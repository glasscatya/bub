"""Helpers for escaping XML-like prompt blocks."""

from __future__ import annotations

from html import escape


def escape_prompt_text(text: str) -> str:
    """Escape dynamic text placed inside prompt tag bodies."""

    return escape(text, quote=False)


def escape_prompt_attr(value: str) -> str:
    """Escape dynamic values placed inside prompt tag attributes."""

    return escape(value, quote=True)
