#!/usr/bin/env python3

from modules.data_reader import read_file


def get_line(tag, date, data, cleaner, source):

    """[TODO: function to read data and get the line to be tweeted]

    Args:
        tag ([TODO:parameter]): [TODO: Hashtag]
        date ([TODO:parameter]): [TODO: Should be "eng" or "esp"]
        data ([TODO:parameter]): [TODO: Data to read from file]
        cleaner ([TODO:parameter]): [TODO: It tells the function
                                     if data should be cleaned]
        source ([TODO:parameter]): [TODO: Data source]

    Returns:
        [TODO: line for the tweet]
    """
    mystr = read_file(data, cleaner)

    mystr = f'{tag}, {date}, {mystr} {source}'

    return mystr


if __name__ == "__main__":
    pass
