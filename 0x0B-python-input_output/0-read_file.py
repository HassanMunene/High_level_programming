#!/usr/bin/python3
"""
The purpose of this module is to read a file
"""

def read_file(filename=""):
    """
    This func reads a file and returns it's content
    """
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
