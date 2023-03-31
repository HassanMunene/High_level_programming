#!/usr/bin/python3
"""
In this module we are declaring a function that reads from
a text file and returns the texts to the standard output
"""


def read_file(filename=""):
    """
    This function takes in the filename
    and then opens it, reads its contents
    and then prints the contents to  the screen
    """

    with open(filename, mode='r', encoding='utf-8') as f:
        contents = f.read()
        print(contents, end='')
