import os

from config import config

from utils import get_youtube_data, create_database, save_data_to_database


def main():
    api_key = os.getenv('YOUTUBE_API_KEY')
    channel_ids = [
        'UCMCgOm8GZkHp8zJ6l7_hIuA',
        'UC6uFoHcr_EEK6DgCS-LeTNA'
    ]

    params = config()

    data = get_youtube_data(api_key, channel_ids)
    create_database('youtube', params)
    save_data_to_database(data, 'youtube', params)


if __name__ == '__main__':
    main()
