#!/usr/bin/env python3

from app.services import get_line, split_string
from app.config import create_api

from datetime import datetime

# import locale
import locale


class TweepyBot:
    """
    A class representing a Twitter bot powered by Tweepy.

    Attributes:
        api: The Twitter API object used for interacting
             with the Twitter platform.
        hashtag: The hashtag to be included in the tweet.
        date_format: The format for the date (either "esp" or "eng").
                     Default is None.
        data: The data to populate the tweet.
        line: The desired line. It can be either "longest" or "random".
              Default is None. If None, the tweet line will be random.
        text: The custom text to be included in the tweet.
              Overrides other tweet components if provided.
        source: The data source for the tweet.
        cleaner: A boolean indicating whether to execute a data cleaner.
                 False by default.

    Methods:
        get_formatted_date():
            Create a formatted date.
            Returns:
                A string with the formatted date.

        prepare_tweet():
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
        text=None,
        data=None,
        line=None,
        source=None,
        cleaner=False
    ):
        self.api = api
        self.hashtag = hashtag
        self.date_format = date_format
        self.text = text
        self.data = data
        self.line = line
        self.source = source
        self.cleaner = cleaner

    def get_formatted_date(self):
        """
        Create a formatted date.

        Returns:
            str: The formatted date.
        """
        try:
            if self.date_format is None:
                return None
            elif self.date_format == "esp":
                # Set the locale to Spanish
                locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

                # Get the current date
                current_date = datetime.now()

                # Format the date as "day de month"
                formatted_date = current_date.strftime("%d de %B")

            elif self.date_format == "eng":
                # Set the locale to English
                locale.setlocale(locale.LC_TIME, 'en_US.UTF-8')

                # Get the current date
                current_date = datetime.now()

                # Format the date as "month day"
                formatted_date = current_date.strftime("%B %d")
            else:
                raise ValueError("Invalid date format")
        except ValueError as e:
            print(f"Error {e}")
            return None

        return formatted_date

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
                    self.get_formatted_date(),
                    self.data,
                    self.line,
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
            text: The string to be published as a tweet or thread.
        """
        try:
            if len(text) <= 240:
                response = self.api.create_tweet(text=text)
                responseStr = "\n************ Response Object ************\
                               \n{}".format(response)
                print(responseStr.lstrip())
            else:
                tweets = split_string(text)
                n_tweets = len(tweets)
                logs = []
                if n_tweets > 1:
                    firstStr = tweets[0] + " [1/%s]" % (str(n_tweets))
                    response = self.api.create_tweet(text=firstStr)
                    i = 2
                    for tweet in tweets[1:]:
                        otherStr = tweet + " [%s/%s]" % (str(i), str(n_tweets))
                        logs.append(response)
                        response = self.api.create_tweet(
                            text=otherStr,
                            in_reply_to_tweet_id=response.data['id']
                        )
                        i += 1
                    logs.append(response)
                for i, item in enumerate(logs, start=1):
                    logsStr = "\n************ Response Object ************\
                               \nResponse {}: {}\n".format(i, item)
                    print(logsStr.lstrip())
            print("Tweeted successfully!")
        except Exception as e:
            print(f"An error occurred while creating the tweet: {str(e)}")

    def __str__(self):
        """repr method.

        Args:
            None

        """
        representation = "\n[TweepyBot]\
                          \nAPI: {}\
                          \nHashtag: {}\
                          \nDate format: {}\
                          \nData: {}\
                          \nLine: {}\
                          \nText: {}\
                          \nSource: {}\
                          \nCleaner: {}\n".format(self.api,
                                                  self.hashtag,
                                                  self.date_format,
                                                  self.data,
                                                  self.line,
                                                  self.text,
                                                  self.source,
                                                  self.cleaner)
        return representation


if __name__ == "__main__":
    pass
