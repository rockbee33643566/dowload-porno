# ydl_config.py
"""Конфигурация для yt-dlp с оптимизацией под быструю загрузку."""

YDL_OPTS = {
    # === Имя файла ===
    "outtmpl": "%(title)s [%(id)s].%(ext)s",

    # === Выбор формата ===
    # Лучшее видео (до 1080p) + лучшее аудио, fallback — лучший комбинированный
    "format": "bestvideo[height<=1080]+bestaudio/best[height<=1080]/best",
    "merge_output_format": "mp4",

    # === Ускорение загрузки ===
    # Параллельная загрузка фрагментов HLS/DASH (главный ускоритель)
    "concurrent_fragment_downloads": 16,

    # Внешний загрузчик aria2c (опционально, см. ниже)
    # "external_downloader": "aria2c",
    # "external_downloader_args": ["-x", "16", "-s", "16", "-k", "1M"],

    # Размер буфера и HTTP-чанков
    # "buffer_size": 1024 * 1024,        # 1 MiB буфер
    # "http_chunk_size": 10 * 1024 * 1024,  # 10 MiB чанки (помогает обойти throttling)

    # === Надёжность ===
    "retries": 2,
    "fragment_retries": 5,
    "file_access_retries": 3,
    # "retry_sleep_functions": {
    #     "http": lambda n: min(4 * n, 30),       # экспоненциальная пауза до 30с
    #     "fragment": lambda n: min(4 * n, 30),
    # },
    "skip_unavailable_fragments": True,

    # === Тишина и логи ===
    "quiet": False,             # показывать прогресс
    "no_warnings": True,
    "noprogress": False,

    # === Постобработка ===
    # "writesubtitles": True,
    # "subtitleslangs": ["en", "ru"],
    # "embedsubtitles": True,

    # === Прочее ===
    "ignoreerrors": True,       # не падать на битых видео в списке
    "no_color": True,
    "cachedir": False,          # если нужен кэш — уберите строку
}