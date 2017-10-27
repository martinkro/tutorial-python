# -*- coding:utf-8 -*-

import urllib2
import urllib

if __name__ == "__main__":
    data = {'name':'test'}
    f = urllib2.urlopen(url='http://localhost:8000/test.php',
        data = urllib.urlencode(data))
        
    content = f.read()
    print(content)