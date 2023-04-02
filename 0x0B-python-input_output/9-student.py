#!/usr/bin/python3
"""
we declare a class and initialize some
instance atrributes
and then we crate a function that basically returns
the dictionary representation of the class
this is achieved by use of the __dict__ attribute of the object
"""


class Student:
    """
    a blueprint about a student
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        retrieves the dictionary representation
        of an instance of this class
        """
        return self.__dict__
