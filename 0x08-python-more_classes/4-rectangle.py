#!/usr/bin/python3
"""
Module representation of Rectangle class
and calculates the area and the perimeter of the
rectangle
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

        """
        used to calculate the area of the rectangle
        """
        return (self.__width) * (self.__height)

    def perimeter(self):
        """
        used to calculate the perimeter of the rectangle
        """
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
        show string representation of an object
        """
        s = ""
        for r in range(self.__height):
            for c in range(self.__width):
                s += "#"
            if r != self.__height - 1:
                s += "\n"
        return s

    def __repr__(self):
        """
        represent a string that can be used to
        create a new instance of the object
        """
        return("Rectangle(" + str(self.__width) + "," + str(self.__height) + ")")

