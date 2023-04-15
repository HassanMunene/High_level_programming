#!/usr/bin/python3
"""
This module contains a class that inherits from the rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    The blueprint of square
    """
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)

    def __str__(self):
        """
        return the string representation of the object
        """
        return f"[{self.__class__.__name__}] {self.__size}/{self.__size}"

    def area(self):
        """
        calculate the area of the circle
        """
        return self.__size * self.__size
