#!/usr/bin/python3
"""
Append a string to the already existing file
"""

def append_write(filename="", text=""):
    with open('filename', 'a', encoding='utf-8') as f:
        return(f.write(text))

