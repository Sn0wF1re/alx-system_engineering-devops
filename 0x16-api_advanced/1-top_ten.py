#!/usr/bin/python3
"""
Write a function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit
"""

import requests


def top_ten(subreddit):
    """
    prints titles of first 10 hot posts listed for a given subreddit
    """
    if not subreddit or type(subreddit) is not str:
        print("None")
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "linux:0x16-api_advanced:v1.0.0 (by /u/Sn0wF1re)"
    }
    params = {"limit": 10}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
