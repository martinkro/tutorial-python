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
    x = 237 #62 + 75
    y = 270 #205 + 58 + 10 + 48
    w = 158
    h = 173
    r,g,b = img.getpixel((x,y))
    print("#%02X%02X%02X" % (r,g,b))
    box = (x,y,x+w,y+h)
    region = img.crop(box)
    region.save("game_empty.jpg", "JPEG", quality=95)

def crop_core(img,name,x,y,w,h,typename):
    box = (x,y,x+w,y+h)
    region = img.crop(box)
    region.save(name, typename, quality=95)
    
def crop_toolbar(filename,suffix):
    names = ["protector","signature","settings","multichannel","help"]
    x = 190
    y = 0
    w = 108
    h = 107
    img = Image.open(filename)
    for i in range(5):
        crop_core(img,names[i]+"_"+suffix+".png",x+i*w,y,w,h,"PNG")
def crop_png2(filename):
    img = Image.open(filename)
    r,g,b,a = img.getpixel((1,1))
    print("#%02X%02X%02X" % (r,g,b))
    print (img.mode)
    print (img.size)
    print (img.format)
    x = 190 #62 + 75
    y = 0 #205 + 58 + 10 + 48
    w = 108
    h = 107
    r,g,b,a = img.getpixel((x,y))
    print("#%02X%02X%02X" % (r,g,b))
    box = (x,y,x+w,y+h)
    region = img.crop(box)
    region.save("protector_normal.png", "PNG", quality=95)
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
    #crop_png2("toolbar_normal.png")
    crop_toolbar("toolbar_normal.png","normal")
    crop_toolbar("toolbar_hover.png","hover")
    crop_toolbar("toolbar_select.png","checked")