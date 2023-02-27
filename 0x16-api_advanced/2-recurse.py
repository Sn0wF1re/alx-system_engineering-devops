#!/usr/bin/python3
"""
Contains recursive function to return list
of all hot articles for a given subreddit
"""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    returns a list containing the titles of all hot articles
    for a given subreddit.
    If no results are found for the given subreddit, return None
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16-api_advanced:v1.0.0 (by /u/Sn0wF1re)"
    }
    params = {
        "after": after,
        "count": count
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")

    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
