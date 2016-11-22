#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys
import os
import logging
import shutil

def convert_post(src_dir, dst_dir):
    src_dir = os.path.realpath(src_dir)
    dst_dir = os.path.realpath(dst_dir)
    if os.path.exists(dst_dir) and os.path.isdir(dst_dir):
        shutil.rmtree(dst_dir)
    os.makedirs(dst_dir)
    
    names = os.listdir(src_dir)
    for name in names:
        if name.endswith(".md"):
            src_full_path = os.path.join(src_dir, name)
            dst_full_path = os.path.join(dst_dir, name)
            f = open(src_full_path, "r", encoding="utf-8")
            lines = f.readlines()
            f.close()
            
            f = open(dst_full_path, "w", encoding="utf-8")
            for line in lines:
                if line.find("{% include JB/setup %}") != -1:
                    continue
                f.write(line)
            f.close()

log = logging.getLogger("main")
if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    log.info("start ...")
    
    src_dir = "_posts"
    dst_dir = "temp"
    convert_post(src_dir, dst_dir)
    
    log.info("END.")