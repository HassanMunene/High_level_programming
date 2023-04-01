## sys.argv
The sys module provides functions and variables used to manipulate different parts of the python runtime environment 
This module provides access to some variables and functions that interact strongly with the interpreter

one such variable is *sys.argv* which is a simple list structure. It's main purpose is:
1. it is a list of commandline arguments
2. len(sys.argv) provides the number of command line arguments
3. sys.argv[0] is the name of the current python script

the following below example shows how to add numbers from the commandline rather than from inside the program.

```
import sys

# the total number of arguments
n = len(sys.argv)
print("The total number of arguments passed: {}".format(n))

# the arguments passed
print("The name of the python script is: {}".format(sy.argv[0]))

print("The arguments passed are:", end="")
for i in range (1, n):
	print(sys.argv[i], end="")

sum = 0

for i in range(1, n):
	sum += int(sys.argv[i])

print("The result is: {}".format(sum))
```

