#!/usr/bin/python3
"""
This module appends the a string to a file
and if the file does not exist it creates
another file
"""


def append_write(filename="", text=""):
    """
    This function append a string to a text file
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
