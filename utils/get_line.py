#!/usr/bin/env python3

from datetime import datetime
# import locale
from babel.dates import format_date
from babel.numbers import format_decimal
from utils.data_readers import read_and_delete, read


def get_line_start(date, data, source):

    mystr = read_and_delete(data)

    mystr = f'🤖 #HoyEnLaHistoria, {date}, {mystr} {source}'

    return mystr


def get_line_end(date, data, source):

    mystr = read(data)

    # Tweet each line, then wait one minute and tweet another.
    # Note: this design means the bot runs continuously
    mystr = f'🤖 #HoyEnLaHistoria, {date}, {mystr} {source}'

    return mystr


def get_line_english(date, data, source):

    mystr = read(data)

    # Tweet each line, then wait one minute and tweet another.
    # Note: this design means the bot runs continuously
    mystr = f'🤖 #OnThisDay, {date}, {mystr} {source}'

    return mystr


def get_line_english_start(date, data, source):

    mystr = read_and_delete(data)

    # Tweet each line, then wait one minute and tweet another.
    # Note: this design means the bot runs continuously
    mystr = f'🤖 #OnThisDay, {date}, {mystr} {source}'

    return mystr


if __name__ == "__main__":
    pass
