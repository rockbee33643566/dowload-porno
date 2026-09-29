from pornhub_api.schemas.category import Category
from pornhub_api.schemas.video import Video

from typing import Iterable

from config import BAD_WORDS

def filter_tag(
    tags: Iterable[str],
    bad_words: list[str] = BAD_WORDS
) -> list[str]:
    return [t for t in tags if not any(bw in t.lower() for bw in bad_words)]

def filter_category(
    categories: Iterable[Category],
    bad_words: list[str] = BAD_WORDS
) -> list[Category]:
    return [c for c in categories if not any(bw in c.category.lower() for bw in bad_words)]

def filter_video(
    videos: Iterable[Video],
    bad_words: list[str] = BAD_WORDS
) -> list[Video]:
    return [v for v in videos if not any(bw in v.title for bw in bad_words)]