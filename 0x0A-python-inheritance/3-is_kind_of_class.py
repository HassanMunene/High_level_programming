#!/usr/bin/python3
"""
This module tells us whether an object is an
instance of a class or an instance of a derived class
"""


def is_kind_of_class(obj, a_class):
    """
    a func that tells whether an object is an instance
    of a class or a derived class
    """
    return isinstance(obj, a_class)
