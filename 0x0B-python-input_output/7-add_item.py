#!/usr/bin/python3
"""
This script takes arguments from the command line and then
adds them to a list and then the list is saved
to a json file in a json representation
"""
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
import sys
# sys is the module that will help us interact with the interpreter


# the first thing to do is to get the number of commandline arguments passed.
# remember that argv is just a simple list strucure that contains the cli arguments

n = len(sys.argv)

# using the for loop we iterate through the arguments and then append them to a list.
# so we need to create an empty list first, after assigning them arguments
# then next it to use that list to save it to a json file name add_item.json in a json representation

cli_list = []

for i in range(1, n):
    cli_list.append(sys.argv[i])

save_to_json_file(cli_list, "add_item.json")
