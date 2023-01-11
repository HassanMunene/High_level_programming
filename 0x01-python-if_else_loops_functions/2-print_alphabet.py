#!/usr/bin/python3
#declare a variable that we will use to store the concatenated alphabets
result = ""
#use for loop to iterate over the ASCII values
#use chr() function to produce the character representation of the ASCII value
for i in range(97, 123):
    result = result + chr(i)
    
print(str(result), end="")

