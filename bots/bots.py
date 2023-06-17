#!/usr/bin/python3

from bots.config import create_api

import os
from utils.data_procesors import data_processor_end
from utils.data_procesors import data_processor_start
from utils.data_procesors import data_processor_english
from utils.create_tweet import create_tweet


def tweet_start():
    home = os.getenv("HOME")
    data = '/%s/estudio/tweepy_bot/scrapers/hoy_en_la_historia.txt' % (home)
    api = create_api()
    mystr = data_processor_start(data)
    create_tweet(api, mystr)


def tweet_end():
    home = os.getenv("HOME")
    data = '/%s/estudio/tweepy_bot/scrapers/hoy_en_la_historia.txt' % (home)
    api = create_api()
    mystr = data_processor_end(data)
    create_tweet(api, mystr)


def tweet_english():
    home = os.getenv("HOME")
    data = '/%s/estudio/tweepy_bot/scrapers/today_in_history.txt' % (home)
    api = create_api()
    mystr = data_processor_english(data)
    create_tweet(api, mystr)


if __name__ == "__main__":
    pass
