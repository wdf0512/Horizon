"""抖音电商规则中心 scraper (direct API, no Playwright needed).

Uses the public queryDocArticleList API on op.jinritemai.com.
The ARGUS challenge cookie value is hardcoded; it has been stable since at least 2024.
If the API starts returning empty results, check whether the cookie value changed in the
page source: look for `var e="...",t="..."` in https://op.jinritemai.com/home.
"""

import logging
from datetime import datetime, timezone
from typing import List, Optional

import httpx

from .base import BaseScraper
from ..models import ContentItem, JinriteMaiConfig, SourceType

logger = logging.getLogger(__name__)

_API_URL = "https://op.jinritemai.com/doc/external/open/queryDocArticleList"
_ARTICLE_BASE = "https://op.jinritemai.com/announcement"
# dirId=5 is the public rule/announcement feed (规则变更 + 其他公告)
_DIR_ID = 5
# ARGUS challenge cookie — hardcoded values from the site's JS: var e="4272",t="28791"
_ARGUS_COOKIE = "gfkadpd=4272,28791"
_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Cookie": _ARGUS_COOKIE,
    "Referer": "https://op.jinritemai.com/",
}


class JinriteMaiScraper(BaseScraper):
    """Scrape 抖音电商规则中心 rule announcements via the public article-list API."""

    def __init__(self, config: JinriteMaiConfig, http_client: httpx.AsyncClient):
        super().__init__(config.model_dump(), http_client)
        self.jin_config = config

    async def fetch(self, since: datetime) -> List[ContentItem]:
        if not self.jin_config.enabled:
            return []

        params = {
            "dirId": _DIR_ID,
            "orderType": 3,  # order by update time desc
            "pageIndex": 0,
            "pageSize": self.jin_config.fetch_limit,
        }
        try:
            response = await self.client.get(
                _API_URL,
                params=params,
                headers=_HEADERS,
                follow_redirects=True,
                timeout=30.0,
            )
            response.raise_for_status()
            data = response.json()
        except Exception as e:
            logger.warning("jinritemai: API request failed: [%s] %r", type(e).__name__, e)
            return []

        if data.get("code") != 0:
            logger.warning(
                "jinritemai: API returned error code %s: %s",
                data.get("code"),
                data.get("message"),
            )
            return []

        articles = data.get("data", {}).get("articles", [])
        items = []
        for article in articles:
            item = self._article_to_item(article, since)
            if item:
                items.append(item)

        logger.info("jinritemai: %d items after time filter", len(items))
        return items

    def _article_to_item(self, article: dict, since: datetime) -> Optional[ContentItem]:
        title = str(article.get("title") or "").strip()
        if not title:
            return None

        # createTime is Unix seconds
        ts = article.get("createTime") or article.get("updateTime") or 0
        try:
            published_at = datetime.fromtimestamp(int(ts), tz=timezone.utc)
        except (ValueError, OSError):
            published_at = datetime.now(timezone.utc)

        if published_at < since:
            return None

        # Use Feishu doc URL if available (it's the source document); fall back to list page
        feishu = (article.get("extra") or {}).get("feishuDocUrl", "")
        if feishu and feishu.startswith("https://"):
            url = feishu
        else:
            article_id = article.get("id", "")
            url = f"{_ARTICLE_BASE}#{article_id}" if article_id else _ARTICLE_BASE

        dir_name = article.get("dirName", "")
        native_id = str(article.get("id") or title[:40])

        try:
            return ContentItem(
                id=self._generate_id("jinritemai", "announcement", native_id),
                source_type=SourceType.JINRITEMAI,
                title=title,
                url=url,
                content=title,
                author="抖音电商规则中心",
                published_at=published_at,
                metadata={
                    "category": "compliance-ecommerce",
                    "dir_name": dir_name,
                    "platform": "jinritemai",
                    "article_id": native_id,
                },
            )
        except Exception as e:
            logger.debug("jinritemai: skipping article %r: %r", title, e)
            return None
