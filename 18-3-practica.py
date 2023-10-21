# Чтобы получить данные через API YouTube, необходимо создать API Key.
# Это можно сделать на этой странице: https://console.developers.google.com/.
# Или следуйте https://drive.google.com/file/d/1aERhQpimIlH-6dZHAjnd8-x2DcnGYWDe/view
#
# pip install google-api-python-client
# poetry add google-api-python-client
#
# pip install psycopg2

import os

from utils import get_youtube_data, create_database, save_data_to_database
from config import config



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