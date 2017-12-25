from urllib import request,parse

# url
url = 'http://httpbin.org/get'
url2 = 'http://httpbin.org/post'

# dictionary of query parameters
params = {
    'name1':'value1',
    'name2':'value2'
}
# encoding the querey string
querystring = parse.urlencode(params)
u = request.urlopen(url+'?'+querystring)
u2 = request.urlopen(url,querystring.encode('ascii'))
u2.read()
print(u2.read())
print(u.read())