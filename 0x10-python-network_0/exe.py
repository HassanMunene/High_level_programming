#!/usr/bin/python3
import urllib.request
import urllib.parse
#response = urllib.request.urlopen("https://hassanmunene.tech")
#print(response)
#print(response.status)
#print(response.headers)
#print(response.read())

"""url = 'http://pythonprogramming.net'
values = {
    'q': 'basic'
}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read()
print(respData)"""

try:
    x = urllib.request.urlopen('https://www.google.com/search?q=test')
    print(x.read())
except Exception as e:
    print(str(e))

try:
    url = 'https://www.google.com/search?q=test'
    headers = {}
    headers['User-Agent']='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/114.0'
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    data = response.read()
    saveFile = open('withheaders.txt', 'w')
    saveFile.write(str(data))
    saveFile.close()
except Exception as e:
    print(str(e))

