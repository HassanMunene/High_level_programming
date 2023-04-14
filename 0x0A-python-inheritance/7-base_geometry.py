#!/usr/bin/python3
"""
a module containing an empty class of geometry
"""


class BaseGeometry:
    """
    BaseGeometry blueprint
    """
    def area(self):
        """
        the area of an object is done here
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        used to validate an integer
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
