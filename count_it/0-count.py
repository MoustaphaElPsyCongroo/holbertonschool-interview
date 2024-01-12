#!/usr/bin/python3
"""Module to count keywords of reddit hot articles"""
import requests


def count_words(subreddit, word_list, word_occurences={}, after=""):
    """ "Recursively count keywords in the title of reddit's current hot
    articles"""
    lower_word_list = [word.lower() for word in word_list]

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "wsl2_ubuntu:interview_practice:v1.0"}
    params = {"limit": 100}

    req = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )

    if req.status_code > 300:
        return None

    hot = req.json().get("data")
    after = hot.get("after")

    for child in hot.get("children"):
        titles = child.get("data").get("title")
        lower_words_title = [title.lower() for title in titles.split(" ")]

        for word in lower_words_title:
            word_occurences[word] = word_occurences.setdefault(
                word, 0
            ) + lower_words_title.count(word)

    if after is not None:
        return count_words(subreddit, lower_word_list, word_occurences, after)

    sorted_word_occurences = sorted(
        word_occurences.items(), key=lambda w: (-w[1], w[0])
    )
    for key, value in sorted_word_occurences:
        if value > 0:
            print("{}: {}".format(key, value))

    return word_occurences
