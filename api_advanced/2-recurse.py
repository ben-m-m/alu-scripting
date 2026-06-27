#!/usr/bin/python3
"""Recursively retrieve all hot article titles from a subreddit."""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Return a list of all hot post titles for a subreddit."""
    if after is None:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "python:api_advanced:v1.0 (by /u/anonymous)"
    }
    params = {
        "limit": 100,
        "after": after
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False,
            timeout=10
        )

        if response.status_code != 200:
            return None

        data = response.json().get("data")

        for post in data.get("children", []):
            hot_list.append(post.get("data").get("title"))

        after = data.get("after")

        if after is None:
            return hot_list

        return recurse(subreddit, hot_list, after)

    except Exception:
        return None
