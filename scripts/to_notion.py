#!/usr/bin/env python3
"""Append Horizon daily summaries to Notion pages.

For each enabled language, convert the markdown digest to Notion blocks
and append them to the target page via the Notion API.

Required env vars:
    NOTION_API_KEY            Notion integration token (secret_... or ntn_...).
    NOTION_PAGE_ID_ZH         Target page ID for the Chinese digest.
    NOTION_PAGE_ID_EN         Target page ID for the English digest.

Both page IDs are independent; missing ones are simply skipped.
"""

import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path

NOTION_VERSION = "2022-06-28"
API_BASE = "https://api.notion.com/v1"
MAX_CHILDREN_PER_REQUEST = 100
MAX_RICH_TEXT_LENGTH = 2000


# ---------- HTTP ----------

def notion_api(method: str, path: str, token: str, payload: dict | None = None):
    url = f"{API_BASE}{path}"
    data = json.dumps(payload).encode() if payload else None
    req = urllib.request.Request(
        url,
        data=data,
        method=method,
        headers={
            "Authorization": f"Bearer {token}",
            "Notion-Version": NOTION_VERSION,
            "Content-Type": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read()), resp.status
    except urllib.error.HTTPError as e:
        body = e.read().decode() if e.fp else ""
        try:
            parsed = json.loads(body) if body else {}
        except json.JSONDecodeError:
            parsed = {"raw": body}
        return parsed, e.code


# ---------- Rich text ----------

INLINE_TOKEN = re.compile(
    r"(\*\*([^*]+)\*\*"            # **bold**
    r"|`([^`]+)`"                  # `code`
    r"|\[([^\]]+)\]\(([^)]+)\))"   # [text](url)
)


def _rt(text: str, *, bold: bool = False, code: bool = False, link: str | None = None) -> dict:
    return {
        "type": "text",
        "text": {"content": text, "link": ({"url": link} if link else None)},
        "annotations": {
            "bold": bold,
            "italic": False,
            "strikethrough": False,
            "underline": False,
            "code": code,
            "color": "default",
        },
    }


def _split_long(text: str) -> list[str]:
    if len(text) <= MAX_RICH_TEXT_LENGTH:
        return [text]
    return [text[i:i + MAX_RICH_TEXT_LENGTH] for i in range(0, len(text), MAX_RICH_TEXT_LENGTH)]


def build_rich_text(line: str) -> list[dict]:
    out: list[dict] = []
    pos = 0
    for m in INLINE_TOKEN.finditer(line):
        if m.start() > pos:
            for chunk in _split_long(line[pos:m.start()]):
                out.append(_rt(chunk))
        if m.group(2) is not None:
            for chunk in _split_long(m.group(2)):
                out.append(_rt(chunk, bold=True))
        elif m.group(3) is not None:
            for chunk in _split_long(m.group(3)):
                out.append(_rt(chunk, code=True))
        else:
            for chunk in _split_long(m.group(4)):
                out.append(_rt(chunk, link=m.group(5)))
        pos = m.end()
    if pos < len(line):
        for chunk in _split_long(line[pos:]):
            out.append(_rt(chunk))
    return out or [_rt("")]


# ---------- Markdown → blocks ----------

DETAILS_RE = re.compile(
    r"<details><summary>([^<]*)</summary>\s*<ul>(.*?)</ul>\s*</details>",
    re.DOTALL,
)
LINK_RE = re.compile(r'<a href="([^"]+)">([^<]+)</a>')
ANCHOR_RE = re.compile(r'<a id="[^"]*"></a>')


def _block(type_: str, **payload) -> dict:
    return {"object": "block", "type": type_, type_: payload}


def _details_to_toggle(summary_text: str, ul_inner: str) -> dict:
    children = [
        _block("bulleted_list_item", rich_text=[_rt(title, link=url)])
        for url, title in LINK_RE.findall(ul_inner)
    ]
    return _block(
        "toggle",
        rich_text=[_rt(summary_text.strip() or "Details")],
        children=children,
    )


def markdown_to_blocks(md: str) -> list[dict]:
    md = ANCHOR_RE.sub("", md)
    blocks: list[dict] = []
    cursor = 0
    for m in DETAILS_RE.finditer(md):
        if m.start() > cursor:
            blocks.extend(_plain_md_to_blocks(md[cursor:m.start()]))
        blocks.append(_details_to_toggle(m.group(1), m.group(2)))
        cursor = m.end()
    if cursor < len(md):
        blocks.extend(_plain_md_to_blocks(md[cursor:]))
    return blocks


def _plain_md_to_blocks(md: str) -> list[dict]:
    blocks: list[dict] = []
    lines = md.split("\n")
    i = 0
    while i < len(lines):
        stripped = lines[i].lstrip().rstrip()

        if not stripped:
            i += 1
            continue

        if stripped == "---":
            blocks.append(_block("divider"))
            i += 1
            continue

        if stripped.startswith("### "):
            blocks.append(_block("heading_3", rich_text=build_rich_text(stripped[4:])))
            i += 1
            continue
        if stripped.startswith("## "):
            blocks.append(_block("heading_2", rich_text=build_rich_text(stripped[3:])))
            i += 1
            continue
        if stripped.startswith("# "):
            blocks.append(_block("heading_1", rich_text=build_rich_text(stripped[2:])))
            i += 1
            continue

        if stripped.startswith("> "):
            quote_lines = []
            while i < len(lines) and lines[i].lstrip().startswith("> "):
                quote_lines.append(lines[i].lstrip()[2:])
                i += 1
            blocks.append(_block("quote", rich_text=build_rich_text("\n".join(quote_lines))))
            continue

        if stripped.startswith("- ") or stripped.startswith("* "):
            blocks.append(_block("bulleted_list_item", rich_text=build_rich_text(stripped[2:])))
            i += 1
            continue

        num_m = re.match(r"^\d+\.\s+(.*)", stripped)
        if num_m:
            blocks.append(_block("numbered_list_item", rich_text=build_rich_text(num_m.group(1))))
            i += 1
            continue

        blocks.append(_block("paragraph", rich_text=build_rich_text(stripped)))
        i += 1

    return blocks


# ---------- Append ----------

def append_to_page(token: str, page_id: str, blocks: list[dict]) -> bool:
    for start in range(0, len(blocks), MAX_CHILDREN_PER_REQUEST):
        chunk = blocks[start:start + MAX_CHILDREN_PER_REQUEST]
        result, status = notion_api(
            "PATCH", f"/blocks/{page_id}/children", token, {"children": chunk}
        )
        if status != 200:
            print(f"    append failed [{status}]: {result}", file=sys.stderr)
            return False
    return True


# ---------- Main ----------

LANG_ENV = {
    "zh": "NOTION_PAGE_ID_ZH",
    "en": "NOTION_PAGE_ID_EN",
}


def main() -> None:
    token = os.environ.get("NOTION_API_KEY")
    if not token:
        print("NOTION_API_KEY not set — skipping Notion sync", file=sys.stderr)
        return

    date_str = sys.argv[1] if len(sys.argv) > 1 else date.today().strftime("%Y-%m-%d")
    any_failed = False

    for lang, env_key in LANG_ENV.items():
        page_id = os.environ.get(env_key, "").strip()
        if not page_id:
            print(f"  · {lang}: {env_key} not set — skipping")
            continue

        summary_path = Path("data/summaries") / f"horizon-{date_str}-{lang}.md"
        if not summary_path.exists():
            print(f"  · {lang}: source missing ({summary_path}) — skipping")
            continue

        md = summary_path.read_text(encoding="utf-8")
        blocks = markdown_to_blocks(md)
        print(f"  · {lang}: appending {len(blocks)} blocks → page {page_id[:8]}…")
        if append_to_page(token, page_id, blocks):
            print(f"  · {lang}: ok")
        else:
            any_failed = True

    if any_failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
