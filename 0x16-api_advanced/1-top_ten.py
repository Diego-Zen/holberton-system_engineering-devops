#!/usr/bin/python3
"""
    Queries the reddit API and prints the titles of the first 10 hot posts
"""
import requests


def top_ten(subreddit):
    headers = {'user-agent': 'API python reddit subscribers'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    r = requests.get(
        url,
        params={'limit': 10},
        headers=headers,
        allow_redirects=False
    )

    if r.status_code != 200:
        return(0)
    else:
        json_data = r.json()
        for title in json_data['data']['children']:
            print(title['data'].get('title'))
