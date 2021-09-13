import requests
from connection import *

from insert_data import *
import pandas as pd
import json


API_KEY = 'AIzaSyDDFYzkfDadstApPBOSwa5GfhvFgLRwBtU'
part = 'snippet'
query = 'python'
max_results = 300
next_page_token = ''


def youtube_search_api(query, part, api_key, **kwargs):
    url = f'https://www.googleapis.com/youtube/v3/search?q={query}&part={part}&key={api_key}&maxResults={max_results}'
    try:
        page_token = kwargs['pageToken']
        print('Page token set')
        url += f'&pageToken={page_token}'
        print(url)
    except Exception as e:
        pass
    response = requests.get(url)
    data = response.json()
    global next_page_token
    next_page_token = data['nextPageToken']
    video_items = data.get('items')
    return video_items

video_items = youtube_search_api(query, part, API_KEY)

filtered_items = []
counter = 0
for item in video_items:
    counter += 1
    filtered_info = {}
    video_id = item.get('id').get('videoId')
    video_detail_url = f'https://youtube.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&id={video_id}&key={API_KEY}'
    response = requests.get(video_detail_url)
    detailed_data = response.json()

    filtered_info['video_id'] = video_id
    filtered_info['snippet'] = {}
    filtered_info['snippet']['title'] = item.get('snippet').get('title')
    filtered_info['snippet']['channel_title'] = item.get('snippet').get('channelTitle')
    filtered_info['snippet']['publish_time'] = item.get('snippet').get('publishTime')
    try:
        filtered_info['snippet']['tags'] = detailed_data.get('items')[0].get('snippet').get('tags')
    except Exception as e:
        filtered_info['snippet']['tags'] = []
    filtered_info['content_details'] = {}
    try:
        filtered_info['content_details']['duration'] = detailed_data.get('items')[0].get('contentDetails').get('duration')
    except Exception as e:
        filtered_info['content_details']['duration'] = ''
    try:
        filtered_info['statistics'] = detailed_data.get('items')[0].get('statistics')
    except Exception as e:
        filtered_info['statistics'] = {}

    filtered_items.append(filtered_info)

    # print(counter)
    if counter < max_results and counter == 49:
        # print('counter', counter)
        video_items = youtube_search_api(query, part, API_KEY, **{'pageToken': next_page_token})
# print(json.dumps(filtered_items))

if __name__ == '__main__':
    conn = create_connection(r'youtube_data.db')
    cursor = conn.cursor()

    insert_data_to_db(cursor, conn, filtered_data=filtered_items)
