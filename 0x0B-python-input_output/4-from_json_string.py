#!/usr/bin/python3
import json
"""
This module contains a function that returns
an object that is a python data strucuture from a
json string
"""


def from_json_string(my_str):
    return json.loads(my_str)

