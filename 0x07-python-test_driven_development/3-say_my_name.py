#!/usr/bin/python3
"""
This module is used to print the first name and last name
thought last name is optional
"""


def say_my_name(first_name, last_name=""):

    """
    This is the function that does the dirty work of printing
    when it is called
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
