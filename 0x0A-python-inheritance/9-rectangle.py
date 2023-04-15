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
    
    def area(self):
        """
        return the area of rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        print string representation of the object
        """
        return "[{}] {}/{}".format(self.__class__.__name__, self.__width,self.__height)
