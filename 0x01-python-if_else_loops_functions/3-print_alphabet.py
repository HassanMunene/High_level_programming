#!/usr/bin/python3

#define a var that will store the alphabets
result = ""
#use for loop to iterate over the ASCII values
#user chr() function to get the character represention of the ASCII values
for i in range(97, 123):
    if i == 101 or i == 113:
        continue
    result = result + chr(i)
print(str(result))
