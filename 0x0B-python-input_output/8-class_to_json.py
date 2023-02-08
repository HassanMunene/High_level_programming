#!/usr/bin/python3
"""
This module returns a dictionary description with
simple data structures
"""

def class_to_json(obj):
    """
    a function to return a dictionary description
    """
    return vars(obj)
