#!/usr/bin/python3
"""
we will import the function write_file and then
call the function with the filename and the text we want
to write to the file we have just entered
"""
write_file = __import__('1-write_file').write_file

nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
print(nb_characters)
