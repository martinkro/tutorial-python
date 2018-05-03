# -*- coding:utf-8 -*-

import sys
import os
from lxml import etree
import codecs

basedir = os.path.abspath(os.path.dirname(__file__))

if __name__ == '__main__':
    print(basedir)
    test_file_path = os.path.abspath(os.path.join(basedir,'testdata/xpath/1677-Android/201805021225.html'))
    #test_file_path = os.path.abspath(os.path.join(basedir,'testdata/xpath/1677-Android/test.html'))
    print(test_file_path)
    
    #html = etree.parse(test_file_path)
    #result = etree.tostring(html,pretty_print=True)
    #print(result)
    f = codecs.open(test_file_path,'r','utf-8')
    content = f.read()
    f.close()
    tree = etree.HTML(content)
    r1 = tree.xpath("div[@class='_2yra0FBSkFDlN4e6yjTR9_']")
    #print(len(r1))
    result = tree.xpath("//*[@class='_2yra0FBSkFDlN4e6yjTR9_']//ul[@class='_27UcK08ukeU35yV9GWQ-dX']")
    
    #print(len(result))
    #print(tree)
    #print(result)
    
    '''
    test = tree.xpath("//*[@class='test']")
    print(test[0].tail)
    s = test[0].xpath('span')
    print(s[0].tail)
    '''
    for node in result:
        #print(node.dump())
        #node = result[i]
        #print(node.attrib)
        cnt_acc = node.xpath("li[@class='_2oCQ4wmWhihJ6o9lv9jYam']")
        #print(cnt_acc[0].text)
        cnt_node = node.xpath("li[@class='EJW1-BRSnCuFDgoH0wzXl']")
        cnt_user = cnt_node[0]
        cnt_match = cnt_node[1]
        #crash_id = node.xpath("//li[@class='main-content']//*[@class='_3N5DUJrUIhsuHzFjQYx0Vh _3lJT0ZmYuLk75Dvy_HkXsI']")
        crash_id = node.xpath("li[@class='main-content']//a/div[@class='_3N5DUJrUIhsuHzFjQYx0Vh _3lJT0ZmYuLk75Dvy_HkXsI']/span")
        
        #print(cnt_user.text)
        #print(cnt_match.text)
        #print(crash_id.dump())
        #print(crash_id[0].tail)
        
        print('%s|%s|%s|%s' % (crash_id[0].tail,cnt_acc[0].text,cnt_user.text,cnt_match.text))
        #print(len(crash_id))
        