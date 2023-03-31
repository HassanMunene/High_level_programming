#!/usr/bin/python3
"""
This script contains a function that accepts an object
and then converts the object to a json string
"""
import json


def to_json_string(my_obj):
    """
    convert to json string
    using dumps()
    """
    json_string = json.dumps(my_obj)
    return json_string
