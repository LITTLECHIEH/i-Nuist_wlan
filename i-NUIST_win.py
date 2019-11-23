
import requests
import base64

def wlan_login(tele_num):
    login_url = "http://a.nuist.edu.cn/index.php/index/login"
    USER_ACCOUNT = str(tele_num)
    DOMAIN_SELECTION = 'ChinaNet'
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
    tele_num = 18014486721
    status = wlan_login(tele_num)
    # if "用户已登录" in status:
    #     print("status")

    print(status)
    # wlan_logout()