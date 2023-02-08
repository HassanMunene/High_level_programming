#!/usr/bin/python3
import json
"""
This module contains a function that creates an
object from a json file
"""


def load_from_json_file(filename):
    """
    creates an object from a json file
    """
    with open(filename, "r", encoding="utf-8") as f:
        json_obj = f.read()
        if not len(json_obj):
            return None
        return json.loads(json_obj)
