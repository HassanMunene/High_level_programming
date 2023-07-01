#!/usr/bin/python3
"""
This script takes in a URL, sends a request to it
then displays the vlue of the variable X-Request-Id
which is in the response header
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    response_id = response.headers.get("X-Request-Id")
    print(response_id)
