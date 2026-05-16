#!/usr/bin/env python3
"""Push Horizon daily summaries (zh + en) into an Obsidian vault repo.

Reads data/summaries/horizon-{date}-{lang}.md and commits each to
{OBSIDIAN_VAULT_REPO} at {OBSIDIAN_VAULT_PATH}/horizon-{date}-{lang}.md
using the GitHub Contents API.

Required env vars:
    OBSIDIAN_VAULT_TOKEN   GitHub PAT with write access to the vault repo.

Optional env vars:
    OBSIDIAN_VAULT_REPO    Defaults to "wdf0512/Obsidian-Defang".
    OBSIDIAN_VAULT_PATH    Defaults to "Horizon".
"""

import base64
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path

DEFAULT_REPO = "wdf0512/Obsidian-Defang"
DEFAULT_PATH = "Horizon"
LANGS = ("zh", "en")


def github_api(method: str, path: str, token: str, payload: dict | None = None):
    url = f"https://api.github.com{path}"
    data = json.dumps(payload).encode() if payload else None
    req = urllib.request.Request(
        url,
        data=data,
        method=method,
        headers={
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json",
            "Content-Type": "application/json",
            "User-Agent": "Horizon-Bot/1.0",
        },
    )
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read()), resp.status
    except urllib.error.HTTPError as e:
        body = e.read().decode() if e.fp else ""
        return (json.loads(body) if body else {}), e.code


def push_one(token: str, repo: str, vault_path: str, date_str: str, lang: str) -> bool:
    summary_path = Path("data/summaries") / f"horizon-{date_str}-{lang}.md"
    if not summary_path.exists():
        print(f"  · {lang}: source missing ({summary_path}) — skipping")
        return True

    file_path = f"{vault_path.rstrip('/')}/horizon-{date_str}-{lang}.md"
    encoded = base64.b64encode(summary_path.read_bytes()).decode("ascii")

    existing, status = github_api("GET", f"/repos/{repo}/contents/{file_path}", token)
    sha = existing.get("sha") if status == 200 else None

    payload: dict = {
        "message": f"horizon: daily digest {date_str} ({lang})",
        "content": encoded,
    }
    if sha:
        payload["sha"] = sha

    result, status = github_api(
        "PUT", f"/repos/{repo}/contents/{file_path}", token, payload
    )
    if status in (200, 201):
        url = result.get("content", {}).get("html_url", "")
        print(f"  · {lang}: ok → {url}")
        return True
    print(f"  · {lang}: FAILED [{status}] {result}", file=sys.stderr)
    return False


def main() -> None:
    token = os.environ.get("OBSIDIAN_VAULT_TOKEN")
    if not token:
        print("OBSIDIAN_VAULT_TOKEN not set — skipping Obsidian push", file=sys.stderr)
        return

    repo = os.environ.get("OBSIDIAN_VAULT_REPO", DEFAULT_REPO)
    vault_path = os.environ.get("OBSIDIAN_VAULT_PATH", DEFAULT_PATH)
    date_str = sys.argv[1] if len(sys.argv) > 1 else date.today().strftime("%Y-%m-%d")

    print(f"Pushing digest {date_str} → {repo}:{vault_path}/")
    ok = all(push_one(token, repo, vault_path, date_str, lang) for lang in LANGS)
    if not ok:
        sys.exit(1)


if __name__ == "__main__":
    main()
