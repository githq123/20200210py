#encoding:utf-8
import urllib.request as urllib2
import urllib

url="http://www.baidu.com"
#请求的url

res=urllib2.urlopen(url,data=None)

print(res)
print(res.read())
print(res.readline())
print(res.readlines())
print(res.getcode())
print(res.geturl())
print(res.read().decode('utf-8'))