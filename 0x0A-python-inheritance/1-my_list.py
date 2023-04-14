#!/usr/bin/python3
"""
This module shows a class MyList tha inherit from
the well known list class
so it will inherit all the public methods and attributes such as append
It also inherits the sort methos
"""


class MyList(list):
    """
    a blueprint of MyList a subclass of list
    that inherits all the things of list
    it also adds its own method print_sorted()
    """
    def print_sorted(self):
        """
        print the list in a sorted way, ascending order
        """
        list_t = self[:]
        list_t.sort()
        print(list_t)
