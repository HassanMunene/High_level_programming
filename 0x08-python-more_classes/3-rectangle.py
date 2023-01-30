#!/usr/bin/python3
"""
This module is creates a class that defines
a rectangle, its area and perimeter and uses
the __str__ and __repr__ methods
"""


class Rectangle:
    """
    A blue print of a rectangle
    """

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(width) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        calculates the are of a rectangle
        """
        return (self.__width) * (self.__height)

    def perimeter(self):
        """
        calculates the perimeter of a rectangle
        """

        if self.__width == 0 and self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
        Returns human readable string of
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        s = ""
        for r in range(self.__height):
            for c in range(self.__width):
                s += "#"
            if r != self.__height - 1:
                s += "\n"
        return s
