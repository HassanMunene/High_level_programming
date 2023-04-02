#!/usr/bin/python3

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
