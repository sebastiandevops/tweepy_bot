#!/usr/bin/env python3

from app.services import get_line, create_tweet
from app.config import create_api


class TweepyBot:
    """TweepyBot class

    Attributes:
        api (str): Twitter API object.
        tag (str): Hashtag for the tweet.
        date (str): Formatted date for the tweet.
        data (str): Data to populate the tweet.
        source (str): Data source for the tweet.
        cleaner (boolean): Parameter to execute data cleaner.
                       It is false by default.
    """
    def __init__(
        self,
        api=create_api(),
        tag="🤖",
        date="",
        data="",
        text="",
        source="",
        cleaner=False
    ):
        self.api = api
        self.tag = tag
        self.date = date
        self.text = text
        self.data = data
        self.source = source
        self.cleaner = cleaner

    def get_tweet(self):
        """Function to get the line to post to Twitter

        Returns:
            mystr (str): String to be posted
        """
        if self.text != "":
            mystr = self.text
        else:
            mystr = get_line(
                self.tag,
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
                          \nTag: {}\
                          \nDate: {}\
                          \nData: {}\
                          \nSource: {}\
                          \nCleaner: {}".format(self.api,
                                                self.tag,
                                                self.date,
                                                self.data,
                                                self.source,
                                                self.cleaner)
        return representation


if __name__ == "__main__":
    pass
