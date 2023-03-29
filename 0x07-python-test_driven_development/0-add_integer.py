#!/usr/bin/env python3
"""
This module adds two integers that is a and b
a and b must be integers or floats, otherwise raise TypeError exception
with message "a must be an integer or b must be an integer
if a and b are floats they must be first casted to integers
"""
def add_integer(a, b=98):
    """
    will be used two add two integers and
    return results
    """
    if type(a) is float:
        a = int(a)
    else:
        a = a
    
    if type(b) is float:
        b = int(b)
    else:
        b = b

    if a is None or type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")

    if type(a) is str:
        raise TypeError("a must be an integer")

    return a + b



