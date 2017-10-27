# -*- coding:utf-8 -*-
import sys
import os
from PIL import Image

if __name__ == "__main__":
    print("zoom image ...")
    img = Image.open("../testdata/logo.png")
    print (img.mode)
    print (img.size)
    print (img.format)
    (x,y) = img.size
    x = x/2
    y = y/2
    out = img.resize((x,y),Image.ANTIALIAS)
    out.save("logo.png", "PNG", quality=95)
    img.close()