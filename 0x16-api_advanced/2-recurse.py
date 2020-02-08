#!/usr/bin/python3
"""
    Queries the reddit API and returns a list containing all titles
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    headers = {'user-agent': 'API python reddit subscribers'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    r = requests.get(
        url,
        params={'after': after},
        headers=headers,
        allow_redirects=False
    )

    if r.status_code != 200:
        return(None)
    else:
        json_data = r.json()
        after = json_data['data'].get('after')
        for title in json_data['data']['children']:
            hot_list.append(title['data'].get('title'))
        if after is None:
            return(hot_list)
        else:
            return(recurse(subreddit, hot_list, after))
