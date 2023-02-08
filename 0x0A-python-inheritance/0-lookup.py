#!/usr/bin/python3
"""
This module returns the list of all available
attributes and methods of an object
"""


def lookup(obj):
    """
    returns the list of available attr and methods
    """
    return list(dir(obj))
