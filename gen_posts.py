#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys
import os
import logging
import time
import datetime
import random
import shutil

log = logging.getLogger("GenPosts")
if __name__ == "__main__":

    logging.basicConfig(level=logging.DEBUG)
    log.info("start ...")
    
    name_suffix = ['hello-world', 'sample', 'python-design-pattern-singleton', 'c++-design-pattern-singleton']
    titles = ['Hello,World', 'Sample', 'Python Design Pattern:Singleton', 'C++ Design Pattern:Singleton']
    
    content_template = "---\nlayout: post\ntitle: \"%s\"\ndate:%s\n---\n\n"
    
    temp_posts = "posts"
    if os.path.exists(temp_posts) and os.path.isdir(temp_posts):
        shutil.rmtree(temp_posts)
    os.makedirs(temp_posts)
    
    start_time = datetime.datetime.now()
    for i in range(365*2):
        cur_time = start_time - datetime.timedelta(days=i)
        str_time = cur_time.strftime("%Y-%m-%d")
        
        idx = random.randint(0,3)
        #print("%d:%s" % (idx, str_time))
        
        filename = "%s/%s-%s.md" % (temp_posts,str_time, name_suffix[idx])
        content = content_template % (titles[idx], str_time)
        log.debug("filename:%s" % filename)
        
        f = open(filename, "w", encoding="utf-8")
        f.write(content)
        f.close()
    
    log.info("END.")