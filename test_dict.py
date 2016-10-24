# -*- coding:utf-8 -*-

import sys
import os

unity_crc_list = [0x12345678,0x23444444]
unity_offset_list = [(0,0,0),(0,0,0)]
unity_dict = dict(zip(unity_crc_list, unity_offset_list))
if __name__ == "__main__":
    print ("[+] test dict ...")
    dict_a = dict()
    dict_a[12444] = 3333
    dict_a[3333] = "33333"
    for key,value in dict_a.items():
        print("[+]key:%d" % key)
        
    dict_b = {
    0x12345678:(0,0,0),
    0x23444444:(0,0,0)
    }
    
    for key, value in dict_b.items():
        print("[+]key:%d" % key)
    for key, value in unity_dict.items():
        print(key)
        print(value)
        
    if 0x12345678 in unity_dict:
        print(unity_dict[0x12345678])