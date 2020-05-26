#!usr/bin/env
import os
import magic
from PIL import Image, ExifTags

def getfiles(path):
    filespath = []
    nonimagelist = []
    for root, dirs, files in os.walk(path,topdown=False):
        for name in files:
            try:
                fname = os.path.join(root,name)
                #try:
                img = Image.open(fname)
                if(img):
                    fname = fname.replace(path,'')
                    filespath.append(fname)
                #except IOError:
                    #filespath.append("IO Exception")
            except IOError:
                fname = fname.replace(path,'')
                nonimagelist.append("Not image file:" + fname)
    return filespath,nonimagelist
