#!/usr/bin/bash
#This script will receive a url from the cli and then use curl to display the size of the body of the response
#-w is used to specify the output format and the format string here is "%{size_download}"

url=$1

curl -w "%{size_download}\n" -o /dev/null -s $url
