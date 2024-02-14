#!/usr/bin/python3
import requests
'''
3. Count it!
'''


def count_words(subreddit, word_list, after=None, counts=None):
    '''
    Queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords.
    '''
    if counts is None:
        counts = {}

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        'User-Agent': 'LearningScript/1.0 (X11; Linux x86_64; rv:73.0) \
        Python/3.8.5 (Ubuntu 20.04)'
    }
    params = {'limit': 100, 'after': after}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        response.raise_for_status()

        data = response.json()['data']['children']
        for post in data:
            title = post['data']['title']
            for word in word_list:
                word = word.lower()
                title_lower = title.lower()
                if title_lower.count(word) > 0:
                    counts[word] = counts.get(word, 0) +\
                        title_lower.count(word)

        after = response.json()['data']['after']
        if after:
            count_words(subreddit, word_list, after, counts)
        else:
            print_counts(counts)
    except requests.HTTPError as e:
        pass
    except Exception as e:
        pass


def print_counts(counts):
    '''
    Prints the counts of keywords in descending order by count,
    and alphabetically if counts are the same.
    '''
    sorted_counts = sorted(counts.items())
    for word, count in sorted_counts:
        print("{}: {}".format(word.lower(), count))
