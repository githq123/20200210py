#encoding:utf-8
import urllib.request as urllib2
import urllib
import urllib.parse
import os
from click._compat import raw_input
def baidu_search(param):
    headers={

    }
    url ="http://www.baidu.com/s?"+param

    req=urllib2.Request(url,headers=headers)
    res=urllib2.urlopen(req)

    print(res.read())

    dir='./'

    os.chdir(dir)

    file=urllib2.urlopen(url).read()

    open("baidu.html","wb").write(file)

    print("ok")

if __name__=="__main__":

    kw=raw_input("请输入要查找的内容")
    params={
            "wd":kw
        }

    params=urllib.parse.urlencode(params)
    baidu_search(params)