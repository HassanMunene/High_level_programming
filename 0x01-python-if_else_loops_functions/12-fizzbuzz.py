#!/usr/bin/python3
"""
this function prints numbers from 1 to 100
if the number is a multiple of 3 print fizz instead
if the number is a multiple of 5 print buzz instead
if the number is the multiple of of 3 and 5 print fizzbuzz
"""

def fizzbuzz():
    """
    the function that print
    fizz, buzz and fizzbuzz
    """
    for i in range(1, 100):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz ", end="")
        elif i % 3 == 0:
            print("Fizz ", end="")
        elif i % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(i), end="")
