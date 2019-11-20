# !/usr/bin/env python3
# -*- coding=utf-8 -*-
# @Author  : zunsi
# @file: GET_IFNAME.py
# @time: 2019-11-20  16:24:00


import netifaces as ni
import platform

def get_connection_name_from_guid(iface_guids):
    if platform.system() == "Windows":
        import winreg as wr
        # 产生接口名字清单，默认全部写'(unknown)'
        iface_names = ['(unknown)' for i in range(len(iface_guids))]
        # 打开"HKEY_LOCAL_MACHINE"
        reg = wr.ConnectRegistry(None, wr.HKEY_LOCAL_MACHINE)
        # 打开r'SYSTEM\CurrentControlSet\Control\Network\{4d36e972-e325-11ce-bfc1-08002be10318}'
        reg_key = wr.OpenKey(reg, r'SYSTEM/CurrentControlSet\Control\Network\{4d36e972-e325-11ce-bfc1-08002be10318}')
        for i in range(len(iface_guids)):
            try:
                reg_subkey = wr.OpenKey(reg_key, iface_guids[i])

if __name__ == "__main__":
    get_connection_name_from_guid('test01')