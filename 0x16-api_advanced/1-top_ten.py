#!/usr/bin/python3
'''
MODULE: 1. Top Ten
function that prints  the titles of the first 10 hot posts listed
for a given subreddit.
'''
import json
import requests


def top_ten(subreddit):
    '''
     prints  the titles of the first 10 hot posts listed
    5for a given subreddit. and print None if subreddit is invalid
    '''
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    head = {'User-Agent': 'LearningScript/1.0 (X11; Linux x86_64; rv:73.0) \
                Python/3.8.5 (Ubuntu 20.04)'}
    params = {'limit': 10}
    response = requests.get(url, headers=head, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()['data']['children']
        title_list = [post['data']['title'] for post in data]
        for title in title_list:
            print(title)
    else:
        print('None')
