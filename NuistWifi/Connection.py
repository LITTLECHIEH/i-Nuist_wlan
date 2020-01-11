import pywifi
import time


def scan_wifi(ssid) -> bool:
    """
    扫描 wifi
    :return: 如果存在 i-Nuist，则返回 True
    """
    wifi_manager = pywifi.PyWiFi().interfaces()[0]  # 查找可用的 Wifi
    wifi_manager.scan()
    ssid_list = list(map(lambda wifi: wifi.ssid, wifi_manager.scan_results()))
    if ssid in ssid_list:
        return True
    else:
        return False


def connect_wifi(ssid) -> bool:
    """

    :param ssid: 需要连接的Wifi名称
    :return: 连接成功，则返回 True
    """
    timeout_flag = 0  # 防止扫描过长
    begin_time = time.time()

    profile = pywifi.Profile()
    profile.ssid = ssid
    wifi_manager = pywifi.PyWiFi().interfaces()[0]

    while True:  # 扫描 Wifi，直接进行连接操作会报错。
        if time.time() - begin_time > 15:  # 扫描时间过长，结束
            timeout_flag = 1
            break
        if scan_wifi(ssid):  # 扫描到 wifi 结束
            break
        time.sleep(1)

    if timeout_flag == 1:
        return False
    else:
        wifi_manager.connect(profile)
        while wifi_manager.status() == 0:   # 等待硬件进行连接
            time.sleep(0.5)
        return True
