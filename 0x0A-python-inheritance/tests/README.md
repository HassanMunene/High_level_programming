Python's standard library comes equipped wiith a test framework called *doctest*

### doctest
this module programmatically searches python code for pieces of text within comments that look like interactive python sessions.

This module then executes those sessions to confirm that the code referenced by a doctest runs as expected

# Doctest Structure
it is written as though it is a comment, with """ at the top and bottom of the doctest

```
"""
Given two integers, return the sum

>>> add (2, 3)
5
"""
## Incorporating A Doctest into a function

Doctests can sit within a function after the def statement and before the code of the function.

```
def add(a, b):
	"""
	Given two integers return their sum
	
	>>> add(2, 3)
	5
	"""
	return a + b
```

