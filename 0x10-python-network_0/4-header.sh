#!/bin/bash
# This script take in a URL as an arg and sends a GET request to the URL and displays the body of the response, a header var is also specified
curl -sX GET -H "X-School-User-ID: 98" "$1"
