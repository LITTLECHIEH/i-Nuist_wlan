from NuistWifi.Certification import Certification
from NuistWifi.Connection import connect_wifi
import getpass
import demjson
import os
from os import path
import winshell
import time

username = ""
password = ""
domain = ""


def init_account():
    dir_list = os.listdir()
    if "config" not in dir_list:  # 查看文件夹是否存在
        os.mkdir("config")
    if "account.json" in os.listdir("config"):
        account = open("config/account.json", 'r').readline()
        if not account:
            return False
        account = demjson.decode(account)  # 由于存储Json时有引号。故借助demJson库。
        global username, password, domain
        username = account["username"]
        password = account["password"]
        domain = account["domain"]
        return True


def save_account():
    acccount = {'username': username, 'password': password, 'domain': domain}
    output = open("config/account.json", 'w+')
    print(acccount, file=output)


def create_shortcut_to_startup():
    target = path.curdir+"\\WiFi.exe"
    print(target)
    title = '我的快捷方式'

    winshell.CreateShortcut(
        Path=path.join(winshell.startup(), "NUIST WiFi" + '.lnk'),
        Target=target,
        Icon=(target, 0),
        Description=title)


def create_shortcut_to_desktop():
    target = path.curdir+"\\WiFi.exe"
    print(target)
    title = '我的快捷方式'

    winshell.CreateShortcut(
        Path=path.join(winshell.desktop(), "NUIST WiFi" + '.lnk'),
        Target=target,
        Icon=(target, 0),
        Description=title)


def input_infor():
    global username, password, domain
    username = input("请输入账号：")
    password = getpass.getpass("请输入密码（不显示）：")
    domain = input("0. 南京信息工程大学\t 1. 中国移动\t 2. 中国电信\t 3. 中国联通\n请输入用户域（用数字表示）：")
    save_account()
    startup = input("是否开机自启（1：是，2：否）：")
    if startup == "1":
        create_shortcut_to_startup()
    desktop = input("是否创建桌面快捷方式（1：是，2：否）：")
    if desktop == "1":
        create_shortcut_to_desktop()


def run():


    if init_account():  # 若没有输入过密码，则会请求输入
        pass
    else:
        input_infor()
    print("正在等待设备准备ing")
    time.sleep(2)
    connect_wifi('i-NUIST')  # 连接Wifi
    time.sleep(1)
    certification = Certification(username=username, password=password, domain=domain)

    if certification.wlan_login():
        os.system('cls')    # 清空命令行
        print("成功登录！！")
        print("成功登录！！")
        time.sleep(0.5)
    else:
        open("config/account.json", 'w')  # 登录失败则清空文件
        print("登录失败")
        time.sleep(1)
        os.system('cls')
        run()   # 重新输入



if __name__ == '__main__':
    run()
