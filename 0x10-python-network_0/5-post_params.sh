#!/bin/bash
# This script takes in a URL send a POST method to the URL and displays the body of the response, you will have to include param in the POST request
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
