#!/usr/bin/python3
"""
Contains function to return number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns total subscribers for a given subreddit,
    0 if subreddit is invalid
    """
    if not subreddit or type(subreddit) is not str:
        return 0

    url = "http://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "linux:0x16-api_advanced:v1.0.0 (by /u/Sn0wF1re)"}
    response = requests.get(url, headers=headers)
    results = response.json().get("data")
    subs = results.get("subscribers")
    return subs
