# -*- coding:utf-8 -*-

import sys
import os
import json

TP_ENABLE_LOG = 1

TP_LOG_DEBUG = 1
TP_LOG_WARN = 2
TP_LOG_ERROR = 3

def tp_log(level, obj):
    if level > TP_LOG_DEBUG or TP_ENABLE_LOG:
        print(obj)

# parse unity_offset.json        
def UnityOffsetParser:
    def __init__(self, json_path):
        self.json_path = json_path
        self.dict_unity_offset = dict()
    def dump(self):
        for 

if __name__ == "__main__":
    tp_log(TP_LOG_DEBUG, "[+]test json ...")
    filename = "unity_offset.json"
    f = open(filename)
    config = json.load(f)
    f.close()
    
    tp_log(TP_LOG_DEBUG, config)
    
    dict_unity_offset = dict()
    for key,value in config.items():
        version_str = key
        armv7a_crc = value['armeabi-v7a']['crc']
        armv7a_offset = value['armeabi-v7a']['offset']
        x86_crc = value['x86']['crc']
        x86_offset = value['x86']['offset']
        
        a = int(armv7a_crc,16)
        b = int(x86_crc, 16)
        if a in dict_unity_offset or b in dict_unity_offset:
            tp_log(TP_LOG_ERROR, "[!] crc repeat in unity json")
            assert(0)
        
        dict_unity_offset[int(armv7a_crc,16)] = [int(e,16) for e in armv7a_offset]
        dict_unity_offset[int(x86_crc, 16)] = [int(e,16) for e in x86_offset]
    for key,value in dict_unity_offset.items():
        tp_log(TP_LOG_DEBUG, "[+]0x%08x:(0x%08x, 0x%08x, 0x%08x)" % (key, value[0], value[1], value[2]))
        
        