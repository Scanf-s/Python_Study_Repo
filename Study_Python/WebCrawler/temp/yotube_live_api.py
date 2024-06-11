import requests

API_KEY = 'AIzaSyArOhlqzw8AvMtv0m_9VjHA6EtWQLnY2SA'
SEARCH_URL = 'https://www.googleapis.com/youtube/v3/search'
VIDEO_URL = 'https://www.googleapis.com/youtube/v3/videos'
CHANNEL_URL = 'https://www.googleapis.com/youtube/v3/channels'


def get_live_streams(api_key):
    search_params = {
        'part': 'snippet',
        'eventType': 'live',
        'type': 'video',
        'key': api_key,
        'q': "게임",
        'maxResults': 50
    }

    response = requests.get(SEARCH_URL, params=search_params)
    results = response.json()['items']

    live_streams = []

    for item in results:
        video_id = item['id']['videoId']
        snippet = item['snippet']

        # Get video details for viewer count
        video_params = {
            'part': 'liveStreamingDetails',
            'id': video_id,
            'key': api_key
        }
        video_response = requests.get(VIDEO_URL, params=video_params)
        video_details = video_response.json()['items'][0]['liveStreamingDetails']

        # Get channel details for channel name
        channel_id = snippet['channelId']
        channel_params = {
            'part': 'snippet',
            'id': channel_id,
            'key': api_key
        }
        channel_response = requests.get(CHANNEL_URL, params=channel_params)
        channel_details = channel_response.json()['items'][0]['snippet']

        live_streams.append({
            'title': snippet['title'],
            'thumbnail': snippet['thumbnails']['high']['url'],
            'channel_name': channel_details['title'],
            'viewers': video_details.get('concurrentViewers', 'N/A')
        })

    return live_streams


live_streams = get_live_streams(API_KEY)
for stream in live_streams:
    print(f"Title: {stream['title']}")
    print(f"Thumbnail: {stream['thumbnail']}")
    print(f"Channel Name: {stream['channel_name']}")
    print(f"Viewers: {stream['viewers']}")
    print('-' * 40)
