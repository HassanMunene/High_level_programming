#!/usr/bin/python3

"""
module for representation of Rectangle class
"""


class Rectangle:
    """
    Rectangle class
    """
    def __init__(self, width=0, height=0):
        self.widht = width
        self.height = height

    @property
    def widht(self):
        return self.__width
    @property
    def height(self):
        return self.__height

    @widht.setter
    def widht(self, value):
        if type(value) != int:
            raise TypeError("widht must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__widht = value
    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("value must be >= 0")
        self.__height = value

    def area(self):
        """
        returns the area of a rectangle
        """
        return self.__width * self.__height
    def perimeter(self):
        """
        returns the perimeter of the rectangle
        """
        return self.__widht * 2 + self.__height * 2

    def __str__(self):
        """
        returns human readable string of the rectangle
        """
        if self.__width == 0 or self.height ==  0:
            s = ""
        for r in range(self.__height):
            for c in range(self.__width):
                s += "#"
            if r != self.__height - 1:
                s += "\n"
        return s
