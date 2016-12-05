#!/usr/bin/env python3
#-*- coding:utf-8 -*-

def is_prime(number):
    if number <= 1:
        return False
    for element in range(2,number):
        if number % element == 0:
            return False
    return True
    
def print_next_prime(number):
    index = number
    while True:
        index += 1
        if is_prime(index):
            return index