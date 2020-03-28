import urllib.request as request
import urllib.parse as parse
import re as regex

# preparing
url = 'http://pythonprogramming.net'
values = {'s': 'basic', 'submit': 'search'}
data = parse.urlencode(values)  # it's url encoding!!!! :D
data = data.encode('utf-8')  # puts data into bytes
req = request.Request(url, data)

# invoking the request
resp = request.urlopen(req)
respData = resp.read()

print(respData)

# find everything in paragraph tags
paragraphs = regex.findall(r'<p>(.*?)</p>', str(respData))

for eachP in paragraphs:
    print(eachP)
