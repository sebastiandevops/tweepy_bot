#!/usr/bin/python3

from modules.get_line import get_line
from modules.create_tweet import create_tweet


def tweet(api, tag, date, data, source, cleaner=False):
    """[TODO: Function to publish a tweet or thread using the Twitter API]

    Args:
        api ([TODO:parameter]): [TODO: Twitter API object]
        tag ([TODO:parameter]): [TODO: Hashtag for the tweet]
        date ([TODO:parameter]): [TODO: Formatted date for the tweet]
        data ([TODO:parameter]): [TODO: Data to populate the tweet]
        source ([TODO:parameter]): [TODO: Data source for the tweet]
        cleaner ([TODO:parameter]): [TODO: Parameter to execute data cleaner.
                                     It is false by default]
    """
    mystr = get_line(tag, date, data, cleaner, source)
    create_tweet(api, mystr)


if __name__ == "__main__":
    pass
