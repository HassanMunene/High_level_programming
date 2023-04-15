#!/usr/bin/python3
"""
A module containig a class rectangle that inherits from
BaseGeometry
which is defined in a file in the same directory
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    blueprint of a rectangle
    """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
