# -*- coding:utf-8 -*-


BASIC_ENABLE_LOG = 1
LOG_LEVEL_DEBUG = 1
LOG_LEVEL_WARN = 2
LOG_LEVEL_ERROR = 3

# LOG function
def TP_LOG(level,message,out_func=None):
    if level > LOG_LEVEL_DEBUG or BASIC_ENABLE_LOG:
        if out_func:
            out_func(message)
        else:
            print(message)