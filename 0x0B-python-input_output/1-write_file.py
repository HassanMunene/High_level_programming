#!/usr/bin/python3
"""
This mudule is used to write text to a file and return the
number of characters written
"""


def write_file(filename="", text=""):
    with open(filename, mode='w', encoding='utf-8') as f:
        return(f.write(text))
