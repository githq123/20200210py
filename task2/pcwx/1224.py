import requests
from bs4 import BeautifulSoup
r = requests.get("http://www.zuihaodaxue.cn/zuihaodaxuepaiming2018.html")
r.raise_for_status()
r.encoding = 'utf-8'
soup=BeautifulSoup(r.text)
trs=soup.find_all('tr',class_='alt')
for tr in trs:
    tds=tr.find_all('td')
    uId=tds[0].string
    uName=tds[1].string
    uProvince=tds[2].string
    uGrade=tds[3].string
    uindex=tds[4].string
    print(uId,uName,uProvince,uGrade,uindex)