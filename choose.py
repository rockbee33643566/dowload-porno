from pornhub_api.schemas.category import Category

from typing import Iterable
import random

from config import LEN_TAGS

def choose_tags(
    tags: Iterable[str],
    len_tags: int = LEN_TAGS
) -> list[str]:
    return random.sample(tags, len_tags)

def chose_category(
    categories: Iterable[Category]
) -> Category:
    return random.choice(categories)