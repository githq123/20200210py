import requests
from bs4 import BeautifulSoup
from PIL import Image
def getCookie(url):
    r=requests.get(url)
    cookie=r.cookies
    soup=BeautifulSoup(r.text)
    viewstate=soup.find('input')['value']

    return cookie,viewstate
def getCode(url,headers,cookies):
    r=requests.get(url,headers=headers,cookies=cookies)
    with open('code.jpg','wb') as f:
        f.write(r.content)
    im=Image.open('code.jpg')
    im.show()
    code=input('请输入验证码：')
    return code
def login(url,code,viewstate,headers,cookies):
    postData={
    '__VIEWSTATE':viewstate,
    'txtUserName':'20163283',
    'TextBox2':'hq162306',
    'txtSecretCode':code,
    'RadioButtonList1':'% D1 % A7 % C9 % FA',
    'Button1':'',
    'lbLanguage':'',
    'hidPdrs':'',
    'hidsc':''
    }
    r=requests.post(url,data=postData,headers=headers,cookies=cookies)
    print(r.text)
def main():
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'}
    baseUrl='http://ojw.jxust.edu.cn/'
    codeUrl='http://ojw.jxust.edu.cn/CheckCode.aspx'
    loginUrl='http://ojw.jxust.edu.cn/default2.aspx'
    cookies,viewstate=getCookie(baseUrl)
    code=getCode(codeUrl,headers,cookies)
    login(loginUrl,code,viewstate,headers,cookies)


if __name__ == '__main__':
    main()
