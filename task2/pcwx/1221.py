#网络爬虫库urllib、 urllib2、 urllib3、 wget、 scrapy、 requests(建立在urllib3基础上)
#re(正则表达式) beautifulsoup4 处理爬取数据
#*re、beautifulsoup4
#get()
#HTTP的GET提交不超过1024字节
import requests
from bs4 import BeautifulSoup
#r=requests.get("http://www.baidu.com")
#type(r)
#r.status_code
#r.encoding='utf-8'
#soup=BeautifulSoup(r.text)
#soup=BeautifulSoup(r.text,'lxml')
#with open('textRequest.html','w',encoding='utf-8')as f:
    #f.write(r.text)
#print(r.text)
#type(soup)
#print(soup)
def getHTMLText(url):
    try:
       r=requests.get(url,timeout=30)
       r.raise_for_status()
       r.encoding='utf-8'
       return r.text
    except:
        return ""
html=getHTMLText("http://www.baidu.com")
soup=BeautifulSoup(html)
a=soup.find_all('a')
len(a)
#find、find_all
