#!/usr/bin/python3
"""
A MODULE containing a class rectangle
"""


class Rectangle(BaseGeometry):
    """
    a blueprint of rectangle
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        a func to find the area of the rectangle
        """
        return (self.__width) * (self.__height)
    def print():
        """
        print the rectangle area
        """
        print("[Rectangle] {}/{}".format(self.__width, self.__height))

    def __str__(self):
        """
        magic method
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
        
