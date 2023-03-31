#!/usr/bin/python3
"""
This module imports the read_file() from the read_file.py
it then passes the file to be read in the positional argument
"""
read_file = __import__('0-read_file').read_file

read_file("my_file_0.txt")
