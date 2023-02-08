#!/usr/bin/python3
"""
This module defines a class Student
and has a function that returns the instantiation
of the class
"""

class Student:
    """
    a class to define Student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        to_json function
        """
        return {'first_name': self.first_name, 'last_name': self.last_name, 'age': self.age}
