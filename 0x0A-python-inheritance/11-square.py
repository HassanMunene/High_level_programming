#!/usr/bin/python3
"""
This module contains a class Ssquare that
inherits from a class Rectangle
"""


class Square(Rectangle):
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__size(size, size)
        self.__size = size

    def area(self):
        """
        a func to calculate and return the
        area of a square
        """
        return self.__size ** 2
    def print(self):
        """
        a func to print
        """
        print("[Square] {}/{}".format(self.__size, self.__size))

    def __str__(self):
        """
        return human readable string
        """
        return "[Square {}/{}".format(self.__size, self.__size)
