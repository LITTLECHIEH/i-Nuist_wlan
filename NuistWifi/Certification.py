import base64
import requests
import json


class Certification():
    def __init__(self, username, password, domain):
        """
        :param username: 电话号码或用户名
        :param password: 密码
        :param domain: 认证域。0（南京信息工程大学）、1（中国移动）、2（中国电信）、3（中国联通）
        """
        self.username = username
        self.password = password
        self.domain = domain

    def wlan_login(self) -> bool:
        """
        登录wifi
        :return: 成功登录，即返回 True
        """
        all_domain = {"0": "NUIST", "1": "CMCC", "2": "ChinaNet", "3": "Unicom"}
        login_url = "http://a.nuist.edu.cn/index.php/index/login"

        USER_ACCOUNT = str(self.username)
        DOMAIN_SELECTION = all_domain[self.domain]
        USER_PASSWATD = base64.b64encode(str(self.password).encode())

        login_form = {"username": USER_ACCOUNT,
                      "domain": DOMAIN_SELECTION,
                      "password": USER_PASSWATD,
                      "enablemacauth": "0"}
        login_status = requests.post(url=login_url, data=login_form).content.decode("unicode-escape")
        login_status = json.loads(login_status)

        if login_status["status"] == 1 or login_status["info"] == "用户已登录" \
                or login_status["info"] == "认证成功":
            return True
        else:
            return False

    def wlan_logout(self):
        """
        退出登录
        :return: 状态
        """
        logout_url = "http://a.nuist.edu.cn/index.php/index/logout"
        logout_status = requests.post(logout_url)
        if logout_status:
            return True
        else:
            return False
