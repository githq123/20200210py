import requests
from bs4 import BeautifulSoup
r = requests.get("http://www.zuihaodaxue.cn/zuihaodaxuepaiming2018.html")
r.raise_for_status()
r.encoding = 'utf-8'
soup=BeautifulSoup(r.text)
trs=soup.find_all('tr',class_='alt')
for tr in trs:
    tds=tr.find_all('td')
    if tds[2].string == '江西':
        ls=[]
        for i in range(14):
            ls.append(tds[i].string)
        print(ls)