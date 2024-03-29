#!/usr/bin/python3
"""
This file contains a function that accepts a json string
and converts the string to a python object
"""
import json


def from_json_string(my_str):
    """
    takes in my_str which is json and
    converts it to python object
    """
    python_obj = json.loads(my_str)
    return python_obj
