#!usr/bin/env
import os
from PIL import Image, ExifTags

def getfiles(path,subfolders=False):
    imagefilesread = 0
    nonimagefilesread = 0
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
                    img = Image.open(fname)
                    if (any(img.format == f for f in FORMATS)):
                        imagefilesread += 1
                        filespath.append(imgpathstr(fname,path,img))
                    else:
                        nonimagelist.append(imgpathstr(fname,path,img))
                        nonimagefilesread += 1
                except (IOError,ValueError,RuntimeError) as e:
                    fname = fname.replace(path,'')
                    nonimagelist.append(fname)
                    nonimagefilesread += 1
    else:
        try:
            for item in os.listdir(path):
                if(os.path.isfile(os.path.join(path,item))):
                        try:
                            fname = os.path.join(path,item)
                            img = Image.open(fname)
                            if(img):
                                filespath.append(imgpathstr(fname,path,img))
                                imagefilesread += 1
                        except (IOError,ValueError) as e:
                            fname = fname.replace(path,'')
                            nonimagelist.append(fname)
                            nonimagefilesread += 1
        except FileNotFoundError:
            filespath.append("Folder not found")
    print(f"Images found: {imagefilesread} \nNon-image files found: {nonimagefilesread}")
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
