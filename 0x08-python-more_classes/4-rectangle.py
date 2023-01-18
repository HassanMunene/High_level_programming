#!/usr/bin/python3
"""
Module representation of Rectangle class
"""


class Rectangle:
    """
    class representatiion of a rectangle
    """


    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width
    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("heigth must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height
    def perimeter(self):
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        s = ""
        for r in range(self.__height):
            for c in range(self.__width):
                s += "#"
            if r != self.__height - 1:
                s += "\n"
        return s
