#!usr/bin/env
import os
import magic
from PIL import Image, ExifTags

def getfiles(path):
    filespath = []
    nonimagelist = []
    imgfiles = []
    for root, dirs, files in os.walk(path,topdown=False):
        for name in files:
            try:
                fname = os.path.join(root,name)
                img = Image.open(fname)
                if(img):
                    imgformat   = img.format
                    imgsize     = str(img.size[0]) + "x" +  str(img.size[1])
                    fname       = fname.replace(path,'')
                    filespath.append(imgformat + " " + imgsize + " "  + fname)
                    imgfiles.append(img)
            except IOError:
                fname = fname.replace(path,'')
                nonimagelist.append(fname)
    return filespath,nonimagelist,imgfiles
