#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import unittest
from print_num import WidgetTestCase
from print_num import PrintNumberTestCase
from test_primes import PrimesTestCase

def suite():
    suitePrintNumber = unittest.TestSuite()
    suitePrintNumber.addTest(PrintNumberTestCase('test_print_num'))
    
    suiteWidget = unittest.TestSuite()
    suiteWidget.addTest(WidgetTestCase('testGetSize'))
    suiteWidget.addTest(WidgetTestCase('testReSize'))
    
    suitePrimes = unittest.makeSuite(PrimesTestCase,'test')
    
    
    return unittest.TestSuite((suitePrintNumber,
        suiteWidget,
        suitePrimes))

if __name__=="__main__":
    unittest.main(defaultTest='suite')