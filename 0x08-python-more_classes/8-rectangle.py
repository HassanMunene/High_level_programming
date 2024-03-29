#!/usr/bin/python3
"""
Module representation of a Rectangle class
"""


class Rectangle:
    """
    Rectangle class
    """

    number_of_instances = 0
    print_symbol = "#"

    
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        return area of the rectangle
        """
        return self.__width * self.__height
    def perimeter(self):
        """
        perimeter of the rectangle

        """
        return self.__width * 2 + self.__height * 2
    def __str__(self):
        s = ""
        for r in range(self.__height):
            for c in range(self.__width):
                s += str(self.print_symbol)
            if r != self.__height - 1:
                s += "\n"
        return s
    def __repr__(self):
        return("Rectangle(" + str(str.__width) + ", " + str(self.__height) + ")")
    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of a Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
