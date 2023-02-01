#!/usr/bin/python3
"""
This module creates a class
that defines a rectangle with 
private attributes
"""


class Rectangle:
    """
    class that defines a rectangle
    """

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property

    def width(self):
        return self.__width

    @width.setter

    def width(self, value):
        if type(value) != int:
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value

    @property

    def height(self):
        return self.__height

    @height.setter

    def height(self, value):
        if type(value) != int:
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be >= 0")
        self.__height = value
