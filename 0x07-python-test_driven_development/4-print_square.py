#!/usr/bin/python3
"""
This module print a square made up of #
the size in this case is the length of the square
and as you know the length of the square is equal on
both sides
"""


def print_square(size):
    """
    this is the damn function
    """

    if type(size) is not int:
        raise TypeError("size must be integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
