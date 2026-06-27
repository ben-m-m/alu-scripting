#!/usr/bin/python3
"""Queries Reddit API and returns subscriber count of a subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return number of subscribers for a subreddit or 0 if invalid."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "python:api_advanced:v1.0 (by /u/anonymous)"
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            allow_redirects=False,
            timeout=10
        )

        if response.status_code != 200:
            return 0

        return response.json().get("data", {}).get("subscribers", 0)

    except Exception:
        return 0
