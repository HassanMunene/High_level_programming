#!/usr/bin/python3
"""
This script takes a URL and an email address
sends a post request to the URL with the email paramaters
displays the body of the response
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    response = requests.post(url, data=value)
    print(r.text)
