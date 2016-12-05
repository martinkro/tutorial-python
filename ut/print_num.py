#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import unittest

class PrintNumber(object):
    def __init__(self, num):
        self.num = num
    def print_num(self):
        return self.num
        
class PrintNumberTestCase(unittest.TestCase):
    def test_print_num(self):
        value = PrintNumber(6)
        self.assertEqual(7, value.print_num())
        self.assertFalse(value.print_num()==6)
        
    def setUp(self):
        print('test before')
    def tearDown(self):
        print('test after')
        

class Widget:
    def __init__(self, size=(40,40)):
        self.size = size
    def getSize(self):
        return self.size
    def reSize(self,w,h):
        if w < 0 or h < 0:
            raise ValueError('illegal size')
        else:
            self.size = (w,h)
            return self.size

class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget()
    def tearDown(self):
        self.widget = None
    def testGetSize(self):
        print('Test getSize')
        self.assertEqual(self.widget.getSize(),(40,40))
        
    def testReSize(self):
        print('Test reSize')
        self.assertEqual(self.widget.reSize(50,100),(50,100))
if __name__ == "__main__":
    unittest.main()