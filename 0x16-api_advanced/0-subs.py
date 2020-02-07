#!/usr/bin/python3
"""
    Queries the reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    headers = {'user-agent': 'API python reddit subscribers'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    r = requests.get(url, headers=headers, allow_redirects=False)

    if r.status_code != 200:
        return(0)
    json_data = r.json()
    return json_data['data']['subscribers']
