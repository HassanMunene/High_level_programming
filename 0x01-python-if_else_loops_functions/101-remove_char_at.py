#!/usr/bin/python3
"""
module contains a function that
creates a copy of a string
removes the character at the position specified by n
return the modified string
"""


def remove_char_at(str, n):
    """
    str: the string to be modified
    n: the position of the character
    """
    for i in range(len(str)):
        if i == n:
            str = str[:n] + str[n + 1:]

    return str
