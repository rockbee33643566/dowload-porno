from pornhub_api import PornhubApi
from pornhub_api.schemas.video import Video
from pornhub_api.schemas.category import Category

from typing import Iterable
import string
import random

from config import LENING, LEN_NUM, TAGS, CATEGORY
import choose
import filters

def get_ramdon_lets(len_num: int = LEN_NUM) -> str:
    return random.choices(list(string.ascii_lowercase), k=len_num)

def search_tags(api: PornhubApi) -> list[str]:
    tags = []
    lets = get_ramdon_lets()
    for let in lets:
        tags.extend(
            choose.choose_tags(
                filters.filter_tag(
                    api.video.tags(let).tags
                )
            )
        )

    return tags

def search_category(api: PornhubApi) -> Category:
    return choose.chose_category(
        filters.filter_category(
            api.video.categories().categories
        )
    )

def search_videos(
        api: PornhubApi,
        tags: Iterable[str],
        category: Category,
        page: int
) -> list[Video]:
    return filters.filter_video(
        api.search.search(
            ordering="mostviewed", 
            tags=tags, 
            category=category,
            page=page
        ).videos
    )


def auto_search(
        api: PornhubApi, 
        tags: Iterable[str] | None = TAGS,
        category: Category | None = CATEGORY,
        page: int = 1, 
        lening: int = LENING
    ) -> list[Video]:
    if tags is None:
        tags = search_tags(api)

    print("Нашли теги")
    
    if category is None:
        category = search_category(api)

    print("Нашли категорию")

    videos = search_videos(
        api=api,
        tags=tags,
        category=category,
        page=page
    )

    print("Нашли видео: ", len(videos))

    if len(videos) < lening:
        while len(videos) < lening:
            page += 1
            print("Ищю порно на странице:", page)

            videos.extend(
                search_videos(
                    api=api,
                    tags=tags,
                    category=category,
                    page=page
                )
            )

    trim = lening - len(videos)
    return videos[:trim]
