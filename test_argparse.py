# -*- coding:utf-8 -*-

import argparse
import inspect
import sys

class ArgParser(argparse.ArgumentParser):
    def __init__(self):
        super(ArgParser, self).__init__(
            description = inspect.getdoc(sys.modules[__name__]))
        self.add_argument("--hash", 
            help="hash algorithm",
            choices=('crc', 'md5', 'sha1', 'all'),
            default='md5')
        self.add_argument("--runtest", 
            help="run test",
            action="store_true",
            default=False)
        self.add_argument("-t", "--verbosity", help="increase output verbosity",action='store_true')
        self.add_argument('x', type=int, help="the base")
        #self.add_argument("list", help="list games")
        #self.add_argument("game", help="game name")
        # 互斥参数
        group = self.add_mutually_exclusive_group()
        group.add_argument("-v", "--verbose", action="store_true")
        group.add_argument("-q", "--quiet", action="store_true")
if __name__ == '__main__':
    args = ArgParser().parse_args()
    if args.verbosity:
        print('verbosity turned on')