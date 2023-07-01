#!/usr/bin/python3
"""
This module will take a URL and send a POST request to the URL
to post an email which is passed as a parameter to the url
"""
import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]

    value = {"email": sys.argv[2]}
    data_urlencoded = urllib.parse.urlencode(value).encode('ascii')
    r = urllib.request.Request(url, data_urlencoded)
    with urllib.request.urlopen(r) as response:
        body = response.read()
        print(body.decode(utf-8))
