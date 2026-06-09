"""Content analysis using AI."""

import asyncio
import json
import re
from typing import List, Optional
from tenacity import retry, stop_after_attempt, wait_exponential
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, MofNCompleteColumn

from .client import AIClient
from .prompts import (
    CONTENT_ANALYSIS_SYSTEM, CONTENT_ANALYSIS_USER,
    COMPLIANCE_SCORE_SYSTEM, COMPLIANCE_SCORE_USER,
    DEPENDENCY_RISK_SYSTEM, DEPENDENCY_RISK_USER,
    ECOSYSTEM_SIGNAL_SYSTEM, ECOSYSTEM_SIGNAL_USER,
    TELEGRAM_ZH_SYSTEM, TELEGRAM_ZH_USER,
)
from .utils import parse_json_response
from ..models import ContentItem

DEFAULT_THROTTLE_SEC = 0.0


class ContentAnalyzer:
    """Analyzes content items using AI to determine importance."""

    def __init__(self, ai_client: AIClient):
        self.client = ai_client

    @staticmethod
    def _parse_json_response(response: str) -> Optional[dict]:
        """Try multiple strategies to extract a JSON object from an AI response.

        Returns the parsed dict, or None if all strategies fail.
        """
        return parse_json_response(response)

    def _get_throttle_sec(self) -> float:
        """Return the configured inter-item throttle, clamped to zero or above."""
        config = getattr(self.client, "config", None)
        throttle_sec = getattr(config, "throttle_sec", DEFAULT_THROTTLE_SEC)
        return max(throttle_sec, 0.0)

    def _get_concurrency(self) -> int:
        """Return the configured analysis concurrency, clamped to 1 or above."""
        config = getattr(self.client, "config", None)
        concurrency = getattr(config, "analysis_concurrency", 1)
        return max(concurrency, 1)

    async def analyze_batch(self, items: List[ContentItem]) -> List[ContentItem]:
        throttle_sec = self._get_throttle_sec()
        concurrency = self._get_concurrency()
        semaphore = asyncio.Semaphore(concurrency)

        async def _process(item: ContentItem, index: int, progress_task) -> ContentItem:
            async with semaphore:
                try:
                    await self._analyze_item(item)
                except Exception as e:
                    print(f"Error analyzing item {item.id}: {e}")
                    item.ai_score = 0.0
                    item.ai_reason = "Analysis failed"
                    item.ai_summary = item.title
                if throttle_sec > 0 and index < len(items) - 1:
                    await asyncio.sleep(throttle_sec)
            progress.advance(progress_task)
            return item

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            MofNCompleteColumn(),
            transient=True,
        ) as progress:
            task = progress.add_task("Analyzing", total=len(items))
            coros = [
                _process(item, i, task) for i, item in enumerate(items)
            ]
            analyzed_items = await asyncio.gather(*coros)

        return analyzed_items

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(min=2, max=10)
    )
    async def _analyze_item(self, item: ContentItem) -> None:
        """Analyze a single content item.

        Args:
            item: Content item to analyze (modified in-place)
        """
        # Prepare content section
        content_section = ""
        if item.content:
            # Split off comments if present
            content_text = item.content
            if "--- Top Comments ---" in content_text:
                main, comments_part = content_text.split("--- Top Comments ---", 1)
                content_section = f"Content: {main.strip()[:800]}"
            else:
                content_section = f"Content: {content_text[:1000]}"

        # Prepare discussion section (comments, engagement)
        discussion_parts = []
        if item.content and "--- Top Comments ---" in item.content:
            comments_part = item.content.split("--- Top Comments ---", 1)[1]
            discussion_parts.append(f"Community Comments:\n{comments_part[:1500]}")

        meta = item.metadata
        engagement_items = []
        if meta.get("score"):
            engagement_items.append(f"score: {meta['score']}")
        if meta.get("descendants"):
            engagement_items.append(f"{meta['descendants']} comments")
        if meta.get("favorite_count"):
            engagement_items.append(f"{meta['favorite_count']} likes")
        if meta.get("retweet_count"):
            engagement_items.append(f"{meta['retweet_count']} retweets")
        if meta.get("reply_count"):
            engagement_items.append(f"{meta['reply_count']} replies")
        if meta.get("views"):
            engagement_items.append(f"{meta['views']} views")
        if meta.get("bookmarks"):
            engagement_items.append(f"{meta['bookmarks']} bookmarks")
        if meta.get("upvote_ratio"):
            engagement_items.append(f"upvote ratio: {meta['upvote_ratio']:.0%}")
        if engagement_items:
            discussion_parts.append(f"Engagement: {', '.join(engagement_items)}")
        if meta.get("discussion_url"):
            discussion_parts.append(f"Discussion: {meta['discussion_url']}")
        if meta.get("community_note"):
            discussion_parts.append(f"Community Note: {meta['community_note']}")

        discussion_section = "\n".join(discussion_parts) if discussion_parts else ""

        # Derive a human-readable sub-source label for prompt context
        meta = item.metadata
        if meta.get("subreddit"):
            sub_source = f"r/{meta['subreddit']}"
        elif meta.get("feed_name"):
            sub_source = meta["feed_name"]
        elif meta.get("channel"):
            sub_source = f"@{meta['channel']}"
        elif meta.get("repo"):
            sub_source = meta["repo"]
        else:
            sub_source = item.author or item.source_type.value

        # Choose prompt based on item category
        category = item.metadata.get("category", "") or ""

        if category.startswith("compliance-"):
            user_prompt = COMPLIANCE_SCORE_USER.format(
                title=item.title,
                source=item.source_type.value,
                category=item.metadata.get("dir_name") or category,
                url=str(item.url),
                content_section=content_section,
            )
            system_prompt = COMPLIANCE_SCORE_SYSTEM
        elif category == "dependency-risk":
            user_prompt = DEPENDENCY_RISK_USER.format(
                title=item.title,
                source=item.source_type.value,
                sub_source=sub_source,
                url=str(item.url),
                content_section=content_section,
                discussion_section=discussion_section,
            )
            system_prompt = DEPENDENCY_RISK_SYSTEM
        elif category == "telegram-zh":
            user_prompt = TELEGRAM_ZH_USER.format(
                title=item.title,
                sub_source=sub_source,
                url=str(item.url),
                content_section=content_section,
            )
            system_prompt = TELEGRAM_ZH_SYSTEM
        elif category == "ecosystem-signal":
            user_prompt = ECOSYSTEM_SIGNAL_USER.format(
                title=item.title,
                source=item.source_type.value,
                author=item.author or "Unknown",
                url=str(item.url),
                content_section=content_section,
                discussion_section=discussion_section,
            )
            system_prompt = ECOSYSTEM_SIGNAL_SYSTEM
        else:
            user_prompt = CONTENT_ANALYSIS_USER.format(
                title=item.title,
                source=item.source_type.value,
                sub_source=sub_source,
                author=item.author or "Unknown",
                url=str(item.url),
                content_section=content_section,
                discussion_section=discussion_section,
            )
            system_prompt = CONTENT_ANALYSIS_SYSTEM

        # Get AI completion
        response = await self.client.complete(
            system=system_prompt,
            user=user_prompt,
        )

        # Parse JSON response with robust fallback
        result = self._parse_json_response(response)
        if result is None:
            print(f"Warning: could not parse analysis response for {item.id}, using defaults")
            item.ai_score = 0.0
            item.ai_reason = "Analysis response parse failed"
            item.ai_summary = item.title
            item.ai_tags = []
            return

        # Update item with analysis results
        item.ai_score = float(result.get("score", 0))
        item.ai_reason = result.get("reason", "")
        item.ai_summary = result.get("summary", item.title)
        item.ai_tags = result.get("tags", [])
