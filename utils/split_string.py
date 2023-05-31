#!/usr/bin/env python3

def split_string(string):
    if len(string) > 234:
        # First 234 characters
        first_string = string[:234]
        # Find the last space within the first 234 characters
        last_space_index = first_string.rfind(' ')
        if last_space_index != -1:
            # Truncate to the last space
            first_string = first_string[:last_space_index]
        # Remaining characters after first_string
        remaining_string = string[len(first_string):].strip()
        if len(remaining_string) > 234:
            # First 240 characters from remaining_string
            second_string = remaining_string[:234]
            # Find the last space within the first 240 characters
            last_space_index = second_string.rfind(' ')
            if last_space_index != -1:
                # Truncate to the last space
                second_string = second_string[:last_space_index]
            # Remaining characters after second_string
            third_string = remaining_string[len(second_string):].strip()
        else:
            second_string = remaining_string
            third_string = ""
    else:
        first_string = string
        second_string = ""
        third_string = ""

    return first_string, second_string, third_string
