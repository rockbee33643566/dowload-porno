from pornhub_api import PornhubApi
import yt_dlp

from requests.exceptions import JSONDecodeError
import os

from config import YDL_CONFIG
import search
import files

def main() -> None:
    api = PornhubApi()

    category = search.search_category(api)
    dir_name = category.category

    try:
        os.mkdir(dir_name)
    except FileExistsError:
        pass

    YDL_CONFIG["outtmpl"] = f"./{dir_name}/%(title)s [%(id)s].%(ext)s"

    try:
        videos = search.auto_search(api=api, category=category)
    except ValueError as e:
        print("С такими параметрами порно найти не удалось.")
        print("Перезапустите скрипт или измените параметры(если задавали) что бы попробовать ещё раз.")
        return

    urls = [v.url for v in videos]

    with yt_dlp.YoutubeDL(YDL_CONFIG) as ydl:
        ydl.download(urls)

if __name__ == "__main__":
    main()
