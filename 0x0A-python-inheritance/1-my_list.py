#!/usr/bin/python3
"""
This module represents a list ofa class
"""


class MyList(list):
    """
    a blueprint of MyList a subclass of list
    """
    def print_sorted(self):
        """
        print the list in a sorted way, ascending order
        """
        l = self[:]
        l.sort()
        print(l)
