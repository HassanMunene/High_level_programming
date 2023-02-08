#!/usr/bin/python3

"""
This modules tells whether an object is an exact instance
of a class
"""


def is_same_class(obj, a_class):
    """
    func to tell whether an object is an exact instace of a class
    """
    return type(obj) == a_class
