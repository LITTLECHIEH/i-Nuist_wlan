import requests
import time
import base64

#登录地址
post_addr="http://a.nuist.edu.cn/index.php/index/login"

#构造头部信息
post_header={
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-Requested-With':'XMLHttpRequest',
    'Referer':'http://a.nuist.edu.cn/index.php?url=aHR0cDovL2RldGVjdHBvcnRhbC5maXJlZm94LmNvbS9zdWNjZXNzLnR4dA==',
    'Content-Length': '67',

    'Cookie':'_gscu_1147341576=059821653286gq10; sunriseUsername=123441534;\
    sunriseDomain=NUIST;sunriseRememberPassword=true; sunrisePassword=123456;\
    PHPSESSID=hb0o9bkct2f6ge164oj3vj0me5;think_language=zh-CN',
    'Connection':'keep-alive',
}

#构造登录数据
post_data={'domain':'ChinaNet',
           'enablemacauth':'0',
           'password':base64.b64encode("1233321"),
           'username':'18685097861'
          }
#发送post请求登录网页

z=requests.post(post_addr,data=post_data,headers=post_header)
print(z)
