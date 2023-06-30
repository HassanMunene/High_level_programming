#!/usr/bin/bash
#This script will receive a url from the cli and then use curl to display the size of the body of the response
curl -w "%{size_download}\n" -o /dev/null -s $1
