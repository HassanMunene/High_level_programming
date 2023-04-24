#!/usr/bin/python3
"""
will be used to print mubers from 00 to 99
numbers should be printed in asecending order with 2 digits
each number should be separated by , and space
the last number shoulld be followed by a new line
"""
for i in range(0, 100):
    if i < 10:
        print("0{}, ".format(i), end="")
    elif i > 10 and i < 99:
        print ("{}, ".format(i), end="")
    elif i == 99:
        print("{}".format(i))

