#!/usr/bin/python3

from bots.config import create_api

from utils.data_procesors import get_line_end
from utils.data_procesors import get_line_start
from utils.data_procesors import get_line_english
from utils.data_procesors import get_line_english_start
from utils.create_tweet import create_tweet


def tweet_start(data, source):
    api = create_api()
    mystr = get_line_start(data, source)
    create_tweet(api, mystr)


def tweet_end(data, source):
    api = create_api()
    mystr = get_line_end(data, source)
    create_tweet(api, mystr)


def tweet_english(data, source):
    api = create_api()
    mystr = get_line_english(data, source)
    create_tweet(api, mystr)


def tweet_english_start(data, source):
    api = create_api()
    mystr = get_line_english_start(data, source)
    create_tweet(api, mystr)


if __name__ == "__main__":
    pass
