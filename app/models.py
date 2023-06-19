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
        date_format: The formatted date to be included in the tweet.
        data: The data to populate the tweet.
        text: The custom text to be included in the tweet.
              Overrides other tweet components if provided.
        source: The data source for the tweet.
        cleaner: A boolean indicating whether to execute a data cleaner.
                 False by default.

    Methods:
        get_tweet():
            Retrieves the line to post on Twitter, combining the tweet
            components based on the provided attributes.
            Returns:
                A string representing the tweet content.

        post_tweet(mystr):
            Publishes a tweet or thread using the Twitter API.
            Args:
                mystr: The string to be published as a tweet.

    Usage:
        # Create an instance of TweepyBot
        bot = TweepyBot(api=create_api(), hashtag="🤖", date_format=None,
                        data=None, text=None, source=None, cleaner=False)

        # Retrieve the tweet content
        tweet_content = bot.get_tweet()

        # Post the tweet
        bot.post_tweet(tweet_content)
    """
    def __init__(
        self,
        api=create_api(),
        hashtag="🤖",
        date_format=None,
        data=None,
        text=None,
        source=None,
        cleaner=False
    ):
        self.api = api
        self.hashtag = hashtag
        self.date_format = date_format
        self.text = text
        self.data = data
        self.source = source
        self.cleaner = cleaner

    def prepare_tweet(self):
        """
        Retrieves the line to post on Twitter, combining the tweet components
        based on the provided attributes.

        Returns:
            A string representing the tweet content.
        """
        try:
            if self.text is not None:
                text = f'{self.hashtag} {self.text}'
            elif self.data is None and self.text is None:
                text = "Default tweet."
            else:
                text = get_line(
                    self.hashtag,
                    self.date_format,
                    self.data,
                    self.source,
                    self.cleaner
                )
            return text
        except Exception as e:
            # Handle the exception (e.g., log the error or display a message)
            print(f"An error occurred while generating the tweet: {str(e)}")
            return None

    def post_tweet(self, text):
        """
        Publishes a tweet or thread using the Twitter API.

        Args:
            mystr: The string to be published as a tweet.
        """
        try:
            create_tweet(self.api, text)
        except Exception as e:
            # Handle the exception (e.g., log the error or display a message)
            print(f"An error occurred while posting the tweet: {str(e)}")

    def __str__(self):
        """repr method.

        Args:
            None

        """
        representation = "[TweepyBot]\
                          \nAPI: {}\
                          \nHashtag: {}\
                          \nDate format: {}\
                          \nData: {}\
                          \nSource: {}\
                          \nCleaner: {}".format(self.api,
                                                self.hashtag,
                                                self.date_format,
                                                self.data,
                                                self.source,
                                                self.cleaner)
        return representation


if __name__ == "__main__":
    pass
