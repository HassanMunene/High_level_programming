#!/usr/bin/python3
"""
In this module we are saving the object
into a text file using json representation
"""
import json


def save_to_json_file(my_dict, filename):
    """
    This is the function that does the job of serializing
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json_string = json.dumps(my_dict)
        f.write(json_string)
