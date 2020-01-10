from NuistWifi import certification


if __name__ == '__main__':
    # 认证域使用数字：0（南京信息工程大学）、1（中国移动）、2（中国电信）、3（中国联通）

    tele_num = 18014486721
    password = 123321
    domain = 2

    print(certification.wlan_login(tele_num, password, domain))
