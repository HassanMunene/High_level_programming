#!/usr/bin/python3
"""
This script takes in a URL send a request to the URL
displays the body of the response
if the HTTP status code is >= 400 print "Error code: value"
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    body = response.text

    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(body)
