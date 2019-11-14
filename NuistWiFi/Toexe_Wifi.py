# coding=utf-8

import os
import re
import time
import requests




class connectweb(object):

    def connect_baidu(self):  # 检测目前是否联网
        try:
            requests.get("http://www.baidu.com", timeout=2)
            return 1
        except:
            return 0

    def login(self):  # 模拟上网验证 验证网页几乎都是不同的，下面附上我们学校的， form表单自己根据情况填，用chrome很容易得到post的url和表单
        try:
            # 登录地址
            post_addr = "http://a.nuist.edu.cn/index.php/index/login"

            # 构造头部信息
            post_header = {
                'Host': 'a.nuist.edu.cn',
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0',
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                'Accept-Encoding': 'gzip, deflate',
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-Requested-With': 'XMLHttpRequest',
                'Referer': 'http://a.nuist.edu.cn/index.php?url=aHR0cDovL2RldGVjdHBvcnRhbC5maXJlZm94LmNvbS9zdWNjZXNzLnR4dA==',
                'Content-Length': '67',

                'Cookie': '_gscu_1147341576=059821653286gq10; sunriseUsername=123441534;\
                sunriseDomain=NUIST;sunriseRememberPassword=true; sunrisePassword=123456;\
                PHPSESSID=hb0o9bkct2f6ge164oj3vj0me5;think_language=zh-CN',
                'Connection': 'keep-alive',
            }

            # 构造登录数据
            post_data = {'domain': 'NUIST',
                         'enablemacauth': '0',
                         'password': 'MTgzMzEw',
                         'username': 'xxxxxxx'
                         }
            # 发送post请求登录网页
            z = requests.post(post_addr, data=post_data, headers=post_header)
        except exception as e:
            self.disconnect()
            time.sleep(1)
            self.connect_wifi()

    def disconnect(self):  # 断开wifi
        os.system("netsh wlan disconnect")

    def wifis_nearby(self):  # 查询附近wifi
        p = os.popen("netsh wlan show all")
        content = p.read().decode("gb2312", "ignore")
        temp = re.findall(u"(ssid.*\n.*network type.*\n.*\u8eab\u4efd\u9a8c\u8bc1.*\n.*\u52a0\u5bc6.*\n.*bssid.*\n)",
                          content)
        result = []
        for i in temp:
            name = re.findall(u"ssid.*:(.*)\n", i)[0].replace(" ", "")
            result.append(name)
        return result

    def connect_wifi(self, name='i-NUIST'):  # 连接wifi
        os.system("netsh wlan connect name=%s" % name)

    def checking(self):  # 一直检测是否有断网，如果断网则重新连接
        while 1:
            try:
                if not self.connect_baidu():
                    self.login()
            except:
                pass
            time.sleep(10)


if __name__ == "__main__":
    test = connectweb()
    test.login()