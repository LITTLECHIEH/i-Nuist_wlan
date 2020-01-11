import tkinter as tk
from tkinter import messagebox
import os
import demjson
from NuistWifi.Certification import Certification
from NuistWifi.Connection import connect_wifi


class NuistWifiUI(tk.Tk):
    def __init__(self):
        super().__init__()
        super().title("NUIST Wifi")
        super().geometry("500x400")

        tk.Label(self, text="NUIST WIFI", font=('Helvetica', 40)).place(x=140, y=50)

        self.var_username, self.var_password = [tk.StringVar for i in range(2)]
        self.domain = tk.StringVar(0)  # 设置初始值

        tk.Label(self, text="用户名", font=('Helvetica', 12)).place(x=50, y=160)
        self.username_entry = tk.Entry(self, textvariable=self.var_username, width=50)
        self.username_entry.place(x=160, y=160)
        tk.Label(self, text="密码", font=('Helvetica', 12)).place(x=50, y=200)
        self.password_entry = tk.Entry(self, textvariable=self.var_password, width=50)
        self.password_entry.place(x=160, y=200)
        self.password_entry["show"] = "*"  # 隐藏密码
        self.init_account()

        r1 = tk.Radiobutton(self, text='NUIST', variable=self.domain, value=0, font=('Helvetica', 12)).place(x=50,
                                                                                                             y=240)
        r2 = tk.Radiobutton(self, text='移动', variable=self.domain, value=1, font=('Helvetica', 12)).place(x=150, y=240)
        r3 = tk.Radiobutton(self, text='电信', variable=self.domain, value=2, font=('Helvetica', 12)).place(x=250, y=240)
        r4 = tk.Radiobutton(self, text='联通', variable=self.domain, value=3, font=('Helvetica', 12)).place(x=350, y=240)

        button1 = tk.Button(self, text='登录', command=self.login).place(x=50, y=300)
        button2 = tk.Button(self, text='退出', command=self.quit).place(x=350, y=300)

    def init_account(self):
        dir_list = os.listdir()
        if "config" not in dir_list:  # 查看文件夹是否存在
            os.mkdir("config")
        if "account.json" in os.listdir("config"):
            account = open("config/account.json", 'r').readline()
            account = demjson.decode(account)  # 由于存储Json时有引号。故借助demJson库。
            self.username_entry.insert(0, account["username"])
            self.password_entry.insert(0, account["password"])
            self.domain.set(int(account["domain"]))

    def save_account(self):
        acccount = {'username': self.username_entry.get(), 'password': self.password_entry.get(), 'domain': str(self.domain.get())}
        output = open("config/account.json", 'w+')
        print(acccount, file=output)

    def login(self):
        certification = Certification(username=str(self.username_entry.get()), password=str(self.password_entry.get()),
                                      domain=str(self.domain.get()))
        if connect_wifi('i-NUIST') and certification.wlan_login():
            self.save_account()
            tk.messagebox.showinfo(title='登录情况', message='登录成功')
            self.quit()
        else:
            tk.messagebox.showinfo(title="登录情况", message="登录失败")
