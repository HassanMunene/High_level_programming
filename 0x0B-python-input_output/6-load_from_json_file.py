#!/usr/bin/python3
"""
in this file we will create a python object from
a json string
"""
import json


def load_from_json_file(filename):
    """
    in this function we load the json string to
    python object
    the filename contains json string
    """

    with open(filename, 'r', encoding='utf-8') as f:
        contents = f.read()
        return json.loads(contents)
