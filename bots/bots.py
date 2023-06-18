#!/usr/bin/python3

from utils.get_line import get_line_end
from utils.get_line import get_line_start
from utils.get_line import get_line_english
from utils.get_line import get_line_english_start
from utils.create_tweet import create_tweet


def tweet_start(api, date, data, source):
    mystr = get_line_start(date, data, source)
    create_tweet(api, mystr)


def tweet_end(api, date, data, source):
    mystr = get_line_end(date, data, source)
    create_tweet(api, mystr)


def tweet_english(api, date, data, source):
    mystr = get_line_english(date, data, source)
    create_tweet(api, mystr)


def tweet_english_start(api, date, data, source):
    mystr = get_line_english_start(date, data, source)
    create_tweet(api, mystr)


if __name__ == "__main__":
    pass
