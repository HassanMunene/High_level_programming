#!/usr/bin/python3
"""
This module contains a fucntion that writes a string to
a txt file
if the file does not exist it creates the file and if the 
file contains texts it overites them
"""


def write_file(filename="", text=""):
    """
    write texts to a file
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)

