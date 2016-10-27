# -*- coding: utf-8 -*-

import sys
import os

from tutorials import basic

class Singleton1(object):
    def __new__(cls, *args, **kwargs):
        print("[+] Singleton1 __new__")
        if not hasattr(cls, '_inst'):
            cls._inst = super(Singleton1, cls).__new__(cls, *args, **kwargs)
        return cls._inst
    def __init__(self, *args,**kwargs):
        print("[+] Singleton1 __init__")
        return super(Singleton1,self).__init__(*args, **kwargs)
        
class A(Singleton1):
    def __new__(cls, *args, **kwargs):
        print("[+] class A __new__")
        return super(A,cls).__new__(cls, *args, **kwargs)
    def __init__(self, s):
        print("[+] class A __init__")
        self.s = s
        
def test_class_a():
    print("[+] test class a - repeat call __init__")
    a = A('apple')
    b = A('banana')
    print (id(a), a.s)
    print (id(b), b.s)
    
    
# metaclass
# B() = Singleton2(name, bases, class_dict)() = Singleton2(name, bases, class_dict).__call__
class Singleton2(type):
    def __init__(cls, name, bases, dic):
        print("[+] Singleton2 __init__")
        super(Singleton2,cls).__init__(name, bases, dic)
        cls._instance = None
    def __call__(cls, *args,**kwargs):
        print("[+] Singleton2 __call__")
        if cls._instance is None:
            cls._instance = super(Singleton2,cls).__call__(*args, **kwargs)
        return cls._instance

# class B(metaclass=Singleton2):
class B():
    __metaclass__ = Singleton2
    
    def __new__(cls, *args, **kwargs):
        print("[+] class B __new__")
        return super(B,cls).__new__(cls, *args, **kwargs)
    def __init__(self, s):
        print("[+] class B __init__")
        self.s = s
        
def test_class_b():
    print("[+] test class b - repeat call __init__")
    a = B('apple')
    b = B('banana')
    print (id(a), a.s)
    print (id(b), b.s)
# 返回产生一个实例的函数，这个函数无论调用多少次，都是同一个对象
# 这里返回_singleton，而_singleton内部又引用了instances这个函数内的对象，这就是所谓的闭包。
# 类装饰器在类创建的时候，调用，而不是在类实例化的时候调用
# C = type(name, bases,dict)
def singleton3(cls):
    print("[+] singleton3 ...")
    instances = {}
    def _singleton(*args,**kwargs):
        print("[+] singleton3")
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return _singleton
@singleton3
class C:
    
    def __new__(cls, s):
        print("[+] class C __new__")
        return super(cls).__new__(cls, s)
    
    def __init__(self, s):
        print("[+] class C __init__")
        self.s = s
        
def test_class_c():
    print("[+] test class c - repeat call __init__")
    a = C('apple')
    b = C('banana')
    print (id(a), a.s)
    print (id(b), b.s)

    
def singleton4(cls):
    print("[+] singleton4 start ...")
    print(type(cls))
    instance = cls()   # 没有参数  D()
    print(type(instance))
    print("[+] singleton4 override __call__")
    instance.__call__ = lambda: instance  # 覆盖__call__   instance()
    return instance
@singleton4
class D:
    '''
    def __new__(cls, *args, **kwargs):
        print("[+] class C __new__")
        return super(C,cls).__new__(cls, *args, **kwargs)
    '''
    def __init__(self):
        print("[+] class D __init__")
        self.s = "1"

def test_class_d():
    print("[+] test class d - repeat call __init__")
    a = D()
    b = D()
    print (id(a), a.s)
    print (id(b), b.s)

def singleton5(cls):
    print("[+] singleton5 ...")
    instances = {}
    def _singleton(*args,**kwargs):
        print("[+] singleton5")
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return _singleton
  

def e_echo_bar(self):
    print self.x
    
def e_init(self,a):
    print("[+] e_init")
    self.a = a
'''
def e_new(cls,a):
    print ("[+] e_new")
    return super(E,cls).__new__(cls, *args, **kwargs)
'''
    
def test_class_e():
    E = type('E', (), {'x':'b', 'echo_bar':e_echo_bar, '__init__':e_init})
    E = singleton5(E)
    #print (E)
    #print (E.x)
    #print (E.__dict__)
    
    
    e1 = E('aaa')
    print(e1)
    print(e1.__dict__)
    
    e2 = E('bbb')
    print(e2)
    print(e2.__dict__)
    e2.echo_bar()
    
    
    
    print("[+] C class info")
    print(C.__dict__)
    print(C('a').__dict__)
    
if __name__ == "__main__":
    basic.TP_LOG(basic.LOG_LEVEL_DEBUG, "[+] test singleton")
    
    test_class_a()
    test_class_b()
    test_class_c()
    test_class_d()
    test_class_e()