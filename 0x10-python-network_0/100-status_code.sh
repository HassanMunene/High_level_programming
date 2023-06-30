#!/bin/bash
# sends request to the URL but instead of displaying the whole body it only displays the status code
curl -s -o /dev/null/ -w "%{http_code}" "$1"
