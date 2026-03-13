"""
Helpers for channel reply-language defaults.
"""
from __future__ import annotations

import re

LanguageCode = str

_CJK_RE = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff]")


def detect_user_language(text: str) -> LanguageCode:
    value = str(text or "").strip()
    if not value:
        return "en"
    if _CJK_RE.search(value):
        return "zh"
    return "en"


def response_language_instruction(user_text: str) -> str:
    lang = detect_user_language(user_text)
    if lang == "zh":
        return (
            "The user's latest message is written in Chinese. "
            "Reply in Simplified Chinese."
        )
    return (
        "Default to English. Only switch to another language when the user "
        "clearly writes in that language."
    )


def tr(user_text: str, *, en: str, zh: str) -> str:
    return zh if detect_user_language(user_text) == "zh" else en
