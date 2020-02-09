#encoding:utf-8
import urllib.request as urllib2
import urllib

headers={

}
url="http://www.baidu.com"


#创建请求对象
res=urllib2.Request(url,headers=headers)
print(res.get_full_url())#获取完整url
print(res.get_method())#获取客户端请求方法
print(res.get_header("User-Agent"))#获取浏览器的名称
print(res.get_host())#获取host的名称
print(res.get_type())#获取协议的名称

res.add_header("Connection","keep-alive")
print(res.get_header("Connection"))