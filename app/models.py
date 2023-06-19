#!/usr/bin/env python3

from app.services import get_line, create_tweet
from app.config import create_api


class TweepyBot:
    """
    A class representing a Twitter bot powered by Tweepy.

    Attributes:
        api: The Twitter API object used for interacting
             with the Twitter platform.
        hashtag: The hashtag to be included in the tweet.
        date: The formatted date to be included in the tweet.
        data: The data to populate the tweet.
        text: The custom text to be included in the tweet.
              Overrides other tweet components if provided.
        source: The data source for the tweet.
        cleaner: A boolean indicating whether to execute a data cleaner.
                 False by default.
    """
    def __init__(
        self,
        api=create_api(),
        hashtag="🤖",
        date=None,
        data=None,
        text=None,
        source=None,
        cleaner=False
    ):
        self.api = api
        self.hashtag = hashtag
        self.date = date
        self.text = text
        self.data = data
        self.source = source
        self.cleaner = cleaner

    def prepare_tweet(self):
        """Function to get the line to post to Twitter

        Returns:
            mystr (str): String to be posted
        """
        if self.text is not None:
            mystr = f'{self.hashtag} {self.text}'
        else:
            mystr = get_line(
                self.hashtag,
                self.date,
                self.data,
                self.source,
                self.cleaner
            )
        return mystr

    def post_tweet(self, mystr):
        """Function to publish a tweet or thread using the Twitter API

        Args:
            mystr (str): String to publish.
        """
        create_tweet(self.api, mystr)

    def __str__(self):
        """repr method.

        Args:
            None

        """
        representation = "[TweepyBot]\
                          \nAPI: {}\
                          \nHashtag: {}\
                          \nDate: {}\
                          \nData: {}\
                          \nSource: {}\
                          \nCleaner: {}".format(self.api,
                                                self.hashtag,
                                                self.date,
                                                self.data,
                                                self.source,
                                                self.cleaner)
        return representation


if __name__ == "__main__":
    pass
