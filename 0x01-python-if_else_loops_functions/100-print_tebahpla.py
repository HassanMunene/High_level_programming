#!/usr/bin/python3
"""
prints ASCII alphabet in reverse order
alternating lowercase and uppercase(z lower and Y upper)
you are not allowed to store characters in a variable
not allowed to import any module
output: zYxWvUtSrQpOnMlKjIhGfEdCbA
"""
for i in reversed(range(97, 123)):
    print("{}".format(chr(i)) if i % 2 == 0 
            else "{}".format(chr(i - 32)), end="")
