#!/usr/bin/python3
"""
A module containig a class BaseGeometry
"""


class BaseGeometry:
    """
    a blueprint of baseGeometry
    """
    def are(self):
        """
        a func of area not yet implemented
        """
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """
        a func to validate an integer
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
