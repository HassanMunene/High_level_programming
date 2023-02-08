#!/usr/bin/python3
"""
This module checks whether an object is an instance of
a class that inherited directly or indirectly from a
specified class
"""


def inherits_from(obj, a_class):
    """
    a func to achieve the target of the module
    """
    return isinstance(obj, a_class) and not type(obj) == a_class
