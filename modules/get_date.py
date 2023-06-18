#!/usr/bin/env python3

from datetime import datetime
# import locale
from babel.dates import format_date
from babel.numbers import format_decimal


def get_date(format=""):
    """[TODO: function to create a formatted date]

    Args:
        format ([TODO:parameter]): [TODO: Spanish or English format]

    Returns:
        [TODO: formatted date]
    """
    try:
        if format == "esp":
            # Get the current date
            current_date = datetime.now()

            # Format the date components separately
            day = format_decimal(current_date.day, format='##')
            month = format_date(current_date, format='MMMM', locale='es')

            # Format the date as "month day"
            # Create the formatted date with "de" separator
            formatted_date = f"{day} de {month}"

        elif format == "eng":
            # Get the current date
            current_date = datetime.now()

            # Format the date as "month day"
            formatted_date = current_date.strftime("%B %d")
    except Exception as e:
        e = "format parameter should be [esp] or [eng]"
        print(e)

    return formatted_date
