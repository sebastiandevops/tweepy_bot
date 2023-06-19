#!/usr/bin/python3

# tweepy-bots/bots/config.py
import tweepy
import os


def create_api():
    """
    Authenticates to the Twitter API using the provided environment variables.

    Returns:
        tweepy.Client: An instance of the authenticated Twitter API.

    Raises:
        Exception: If an unexpected error occurs during authentication.

    Note:
        Before calling this function, ensure that the following environment
        variables are set:
        - TWITTER_CONSUMER_KEY: The Twitter API consumer key.
        - TWITTER_CONSUMER_SECRET: The Twitter API consumer secret.
        - TWITTER_ACCESS_TOKEN: The Twitter API access token.
        - TWITTER_ACCESS_TOKEN_SECRET: The Twitter API access token secret.
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
