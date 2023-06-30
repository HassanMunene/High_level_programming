#!/bin/bash
# This script makes a GET request to the URL provided but instead of displaying the whole body it only displays the status code
curl -s -o /dev/null/ -w "%{http_code}" "$1"
