# Чтобы получить данные через API YouTube, необходимо создать API Key.
# Это можно сделать на этой странице: https://console.developers.google.com/.
# Или следуйте https://drive.google.com/file/d/1aERhQpimIlH-6dZHAjnd8-x2DcnGYWDe/view
#
# pip install google-api-python-client
# poetry add google-api-python-client
#
# pip install psycopg2

import os

from src.utils import get_youtube_data, create_database, save_data_to_database
from config import config


def create_database(database_name: str, params: dict):
    """Создание базы данных и таблиц для сохранения данных о каналах и видео."""

    conn = psycopg2.connect(dbname='postgres', **params)
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute(f"DROP DATABASE IF EXISTS {database_name}")
    cur.execute(f"CREATE DATABASE {database_name}")

    conn.close()

    conn = psycopg2.connect(dbname=database_name, **params)

    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE channels (
                channel_id SERIAL PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                views INTEGER,
                subscribers INTEGER,
                videos INTEGER,
                channel_url TEXT
            )
        """)

    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE videos (
                video_id SERIAL PRIMARY KEY,
                channel_id INT REFERENCES channels(channel_id),
                title VARCHAR NOT NULL,
                publish_date DATE,
                video_url TEXT
            )
        """)

    conn.commit()
    conn.close()

def main():
    api_key = os.getenv('YT_API_KEY')
    channel_ids = [
        'UC-OVMPlMA3-YCIeg4z5z23A',  # moscowpython
        'UCwHL6WHUarjGfUM_586me8w',  # highload

    ]
    params = config()

    data = get_youtube_data(api_key, channel_ids)
    create_database('youtube', params)
    save_data_to_database(data, 'youtube', params)


if __name__ == '__main__':
    main()