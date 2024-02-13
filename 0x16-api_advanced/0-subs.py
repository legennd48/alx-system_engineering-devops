#!/usr/bin/python3
'''
MODULE: 0. How many subs?
script that returns toal number of subs on a subreddit
'''
import requests


def number_of_subscribers(subreddit):
    '''
    returns the total number of subscribers
    on a given subreddit
    '''
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'LearningScript/1.0 (X11; Linux x86_64; rv:73.0) \
                Python/3.8.5 (Ubuntu 20.04)'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return response.json()['data']['subscribers']
    else:
        return 0
