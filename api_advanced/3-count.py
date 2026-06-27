#!/usr/bin/python3
"""Recursively count keywords in Reddit hot article titles."""

import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Count occurrences of keywords in hot article titles."""
    if counts is None:
        counts = {}
        for word in word_list:
            word = word.lower()
            counts[word] = counts.get(word, 0)

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
            return

        data = response.json().get("data")

        for post in data.get("children", []):
            words = post.get("data").get("title").lower().split()

            for word in words:
                if word in counts:
                    counts[word] += 1

        after = data.get("after")

        if after is not None:
            return count_words(subreddit, word_list, after, counts)

        sorted_counts = sorted(
            counts.items(),
            key=lambda item: (-item[1], item[0])
        )

        for word, count in sorted_counts:
            if count > 0:
                print("{}: {}".format(word, count))

    except Exception:
        return
