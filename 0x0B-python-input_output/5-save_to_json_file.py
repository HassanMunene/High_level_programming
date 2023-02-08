#!/usr/bin/python3
import json

"""
This module contains a function that
writes an an object to a text file using
json representation
"""

def save_to_json_file(my_obj, filename):
    """
    This function saves to a json file
    """
    with open(filename, "w", encoding="utf-8") as r:
        r.write(json.dumps(my_obj))
