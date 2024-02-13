#!/usr/bin/python3
'''
MODULE: 2. Recurse it!
function that returns  the titles of all hot posts listed
for a given subreddit.
'''
import requests


def recurse(subreddit, hot_list=[], after=None):
    '''
    returns the titles of all hotposts
    for a given subreddit. and print None if subreddit is invalid
    '''
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    head = {'User-Agent': 'LearningScript/1.0 (X11; Linux x86_64; rv:73.0) \
                Python/3.8.5 (Ubuntu 20.04)'}
    params = {'after': after, 'limit': 100}
    response = requests.get(url, headers=head, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()['data']['children']
        after = response.json()['data']['after']
        hot_list += [post['data']['title'] for post in data]

        if after is not None:
            recurse(subreddit, hot_list, after)

        return hot_list
    else:
        return None
