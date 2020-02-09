import requests
def send(mobile,captcha):
    url='https://v.juhe.cn/sms'
    params={
        "moblie":mobile,#手机号
        "tpl_id":"",#模板id
        "tpl_value":"#code=#"+captcha,
        "key":""#AppKey
    }
    response=requests.get(url,params=params)
    result=response.json()
    print(result)

    if result['error_code']==0:
        return True
    else:
        return False


send("手机号(不用加引号)","")