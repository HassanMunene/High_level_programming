#!/usr/bin/python3
"""
This module fetches a url and displays the response
"""
import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()
    print("\t- type: {}\n\t- content: {}\n\t- utf8 content: {}".format(type(html), html, html.decode('utf-8')))
