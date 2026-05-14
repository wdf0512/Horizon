#!/usr/bin/env python3
"""Convert Horizon daily summary to blog MDX and push to personal blog repo."""

import base64
import json
import os
import re
import sys
import urllib.request
import urllib.error
from datetime import date
from pathlib import Path


def extract_counts(content: str) -> tuple[int, int]:
    """Return (item_count, total_fetched) from summary header line."""
    m = re.search(r'从\s*(\d+)\s*条内容中筛选出\s*(\d+)\s*条', content)
    if m:
        return int(m.group(2)), int(m.group(1))
    m = re.search(r'From\s+(\d+)\s+items.*?(\d+)\s+important', content)
    if m:
        return int(m.group(2)), int(m.group(1))
    return 0, 0


def convert_to_mdx(summary_path: Path, date_str: str) -> str:
    content = summary_path.read_text(encoding='utf-8')
    item_count, total_fetched = extract_counts(content)

    # Strip the leading H1 title line
    lines = content.split('\n')
    body_lines = []
    skipped = False
    for line in lines:
        if not skipped and line.startswith('# '):
            skipped = True
            continue
        body_lines.append(line)
    body = '\n'.join(body_lines).lstrip('\n')

    if total_fetched > 0:
        description = f"从 {total_fetched} 条内容中精选 {item_count} 条 AI/ML 重要动态"
    else:
        description = "AI/ML 技术情报日报"

    frontmatter = (
        f'---\n'
        f'title: "AI 技术情报 · {date_str}"\n'
        f'slug: horizon-{date_str}\n'
        f'date: {date_str}\n'
        f'published: true\n'
        f'description: "{description}"\n'
        f'item_count: {item_count}\n'
        f'total_fetched: {total_fetched}\n'
        f'---\n\n'
    )
    return frontmatter + body


def github_api(method: str, path: str, token: str, payload: dict | None = None):
    url = f'https://api.github.com{path}'
    data = json.dumps(payload).encode() if payload else None
    req = urllib.request.Request(
        url,
        data=data,
        method=method,
        headers={
            'Authorization': f'token {token}',
            'Accept': 'application/vnd.github.v3+json',
            'Content-Type': 'application/json',
            'User-Agent': 'Horizon-Bot/1.0',
        },
    )
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read()), resp.status
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        return json.loads(body) if body else {}, e.code


def push_to_blog(mdx_content: str, date_str: str) -> None:
    token = os.environ.get('BLOG_REPO_TOKEN')
    if not token:
        print('BLOG_REPO_TOKEN not set — skipping blog push', file=sys.stderr)
        return

    repo = 'wdf0512/my-blog'
    file_path = f'content/digests/horizon-{date_str}.mdx'
    encoded = base64.b64encode(mdx_content.encode('utf-8')).decode('ascii')

    # Check if file already exists (need sha for updates)
    existing, status = github_api('GET', f'/repos/{repo}/contents/{file_path}', token)
    sha = existing.get('sha') if status == 200 else None

    payload: dict = {
        'message': f'feat(digest): Horizon daily digest {date_str}',
        'content': encoded,
    }
    if sha:
        payload['sha'] = sha

    result, status = github_api('PUT', f'/repos/{repo}/contents/{file_path}', token, payload)
    if status in (200, 201):
        url = result.get('content', {}).get('html_url', '')
        print(f'✅ Pushed to blog: {url}')
    else:
        print(f'❌ Push failed [{status}]: {result}', file=sys.stderr)
        sys.exit(1)


def main() -> None:
    today = date.today().strftime('%Y-%m-%d')
    date_str = sys.argv[1] if len(sys.argv) > 1 else today

    summary_path = Path('data/summaries') / f'{date_str}-summary-zh.md'
    if not summary_path.exists():
        print(f'Summary not found: {summary_path}', file=sys.stderr)
        sys.exit(1)

    mdx = convert_to_mdx(summary_path, date_str)
    push_to_blog(mdx, date_str)


if __name__ == '__main__':
    main()
