# -*- coding:utf-8 -*-
import sys
import os
from PIL import Image

def func_zoom_pic(src,dst,rate):
    img = Image.open(src)
    (x,y) = img.size
    x = int(x * rate)
    y = int(y * rate)
    print(x)
    print(y)
    out = img.resize((x,y),Image.ANTIALIAS)
    print(src)
    out.save(dst, "PNG", quality=95)
    img.close()
def zoom_pic(dir,rate):
    names = os.listdir(dir)
    for name in names:
        if name.endswith(".png"):
            src = os.path.join(dir,name)
            dst = os.path.join(".", name)
            func_zoom_pic(src,dst,rate)
def crop_jpg(filename):
    img = Image.open(filename)
    r,g,b = img.getpixel((63,204))
    print("#%02X%02X%02X" % (r,g,b))
    print (img.mode)
    print (img.size)
    print (img.format)
    x = 62 + 75
    y = 205 + 58 + 10 + 48
    w = 51
    h = 48
    r,g,b = img.getpixel((x,y))
    print("#%02X%02X%02X" % (r,g,b))
    box = (x,y,x+w,y+h)
    region = img.crop(box)
    region.save("icon_qq_password.jpg", "JPEG", quality=95)
if __name__ == "__main__":
    print("zoom image ...")
    '''
    img = Image.open("../testdata/logo.png")
    print (img.mode)
    print (img.size)
    print (img.format)
   
    r,g,b = img.getpixel((10,10))
    print(r,g,b)
    r,g,b = img.getpixel((5,5))
    print("#%02X%02X%02X" % (r,g,b))
    
    (x,y) = img.size
    x = x/2
    y = y/2
    out = img.resize((x,y),Image.ANTIALIAS)
    out.save("logo.png", "PNG", quality=95)
    img.close()
    '''
    #zoom_pic("../testdata", 170*1.0/1757)
    crop_jpg("login.jpg")