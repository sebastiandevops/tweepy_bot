#!/usr/bin/python3

# tweepy-bots/bots/config.py
import tweepy
import os


def create_api():
    """Function to authenticate to Twitter API

    Returns:
        Instance of TwitterAPI
    """
    consumer_key = os.getenv("TWITTER_CONSUMER_KEY")
    consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET")
    access_token = os.getenv("TWITTER_ACCESS_TOKEN")
    access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

    try:
        api = tweepy.Client(
                  consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token=access_token,
                  access_token_secret=access_token_secret
              )
        print("Successfully authenticated!")
        return api
    except Exception as e:
        print(f'Error during authentication: {e}')
