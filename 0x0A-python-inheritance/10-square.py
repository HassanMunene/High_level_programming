#!/usr/bin/python3
"""
This module contains a class that inherits from the rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    The blueprint of square
    """
    def __init__(self,size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        a func to return the area of the square
        """
        return self.__size ** 2

