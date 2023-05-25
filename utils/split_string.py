#!/usr/bin/env python3

def split_string(string):
    if len(string) > 240:
        # First 240 characters
        first_string = string[:240]
        # Find the last space within the first 240 characters
        last_space_index = first_string.rfind(' ')
        if last_space_index != -1:
            # Truncate to the last space
            first_string = first_string[:last_space_index]
        # Remaining characters
        second_string = string[len(first_string):].strip()
    else:
        first_string = string
        second_string = ""

    return first_string, second_string
