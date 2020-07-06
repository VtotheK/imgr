#!usr/bin/env
import os
import magic
from PIL import Image, ExifTags

def getfiles(path,subfolders=False):
    if(path==None):
        return
    FORMATS = ["JPEG","PNG","BMP","GIF","TIFF","PPM"]
    filespath = []
    nonimagelist = []
    fname = ""
    if(subfolders):
        for root, dirs, files in os.walk(path,topdown=False):
            for name in files:
                try:
                    fname = os.path.join(root,name)
                    print(f"reading:{fname}")
                    img = Image.open(fname)
                    if (any(img.format == f for f in FORMATS)):
                        filespath.append(imgpathstr(fname,path,img))
                    else:
                        nonimagelist.append(imgpathstr(fname,path,img))
                except (IOError,ValueError,RuntimeError) as e:
                    fname = fname.replace(path,'')
                    nonimagelist.append(fname)
    else:
        try:
            for item in os.listdir(path):
                if(os.path.isfile(os.path.join(path,item))):
                        try:
                            fname = os.path.join(path,item)
                            img = Image.open(fname)
                            if(img):
                                filespath.append(imgpathstr(fname,path,img))
                        except (IOError,ValueError) as e:
                            fname = fname.replace(path,'')
                            nonimagelist.append(fname)
        except FileNotFoundError:
            filespath.append("Folder not found")
    return filespath,nonimagelist


def imgpathstr(fname,path,img):
    imgformat   = img.format
    imgsize     = str(img.size[0]) + "x" +  str(img.size[1])
    fname       = fname.replace(path,'')
    return fname

def isnumber(c):
    if(len(c) < 1):
       return False
    for i in range(len(c)):
        if(not ord(c[i]) > 47 or not ord(c[i]) < 58):
            return False
    if(int(float(c)) == 0):
        return False
    return True
