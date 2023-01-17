#!/usr/bin/python
import sys

def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as exc:
        sys.stderr.write("Exception: " + str(exc) + "\n")
        return None
