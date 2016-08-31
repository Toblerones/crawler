import urllib
import urllib2
import cookielib
import json

cookie = cookielib.CookieJar()
handler=urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
response = opener.open('https://credit.hsbc.com.au/ccol/ccol')
for item in cookie:
    print 'Name = '+item.name
    print 'Value = '+item.value

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'   
headers = { 'User-Agent' : user_agent }   

ajaxRequest={'cmd': 'logonStep1', 'shortCardNumber': '111111111111'}

url = 'https://credit.hsbc.com.au/ccol/ccol'

req = urllib2.Request(url) 
req.add_header('Content-Type', 'application/json1')
response = urllib2.urlopen(req, json.dumps(ajaxRequest)) 
the_page = response.read()

print the_page