import urllib.request as request
import urllib.parse as parse

#x = request.urlopen('https://www.google.com')
# print(x.read())

'''
# preparing the request
url = 'http://pythonprogramming.net'
values = {'s': 'basic', 'submit': 'search'}
data = parse.urlencode(values)  # it's url encoding!!!! :D
data = data.encode('utf-8')  # puts data into bytes
req = request.Request(url, data)

# invoking the request
resp = request.urlopen(req)

# reading data
respData = resp.read()

print(respData)
'''

'''
try:
    x = request.urlopen('https://www.google.com/search?q=test')

    print(x.read())

except Exception as e:
    print(str(e))
'''

try:
    url = 'https://www.google.com/search?q=test'
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    req = request.Request(url, headers=headers)
    resp = request.urlopen(req)
    respData = resp.read()

    saveFile = open('withHeaders.txt', 'w')
    saveFile.write(str(respData))
    saveFile.close()

except Exception as e:
    print(str(e))
