import argprocessor as ip
import irutil 
import oututil
import mainargparser
from datetime import datetime,date,time
import errorwindow 
from tkinter import *
from tkinter import filedialog

def startconversion(arg):
    if(arg.filepath is None or arg.filepath == ""):
        return
    args = {}
    today               = date.today()
    now                 = datetime.now()
    current_time        = time(now.hour,now.minute,now.second)
    dirname             = str(datetime.combine(today,current_time))
    outputpath          = (arg.outputpath,arg.filepath)[arg.outputpath == "" or arg.outputpath is None]
    fcreated, message, outfolder = oututil.createoutputdir(outputpath,dirname)
    if(not fcreated):
        errorwindow.ErrorWindow(root=arg.master,description="No output folder defined!")
        print(f"Could not create output folder, reason: {message}")
        return
    userextension = None
    args["maxheight"] = 0
    args["maxwidth"]  = 0
    if(not arg.filepath):
        errorwindow.ErrorWindow(root=arg.master, description="No destination folder specified")
        return
    if(arg.imglist.size() < 1):
        errorwindow.ErrorWindow(root=arg.master,description="No images loaded")
        return
    elif(len(arg.imglistselections) < 1):
        print(arg.imglistselections)
        errorwindow.ErrorWindow(root=arg.master,description="No images selected")
        return
    elif(arg.val_ckbtn_maxheight.get() == 0 and arg.val_ckbtn_maxwidth.get() == 0):
        errorwindow.ErrorWindow(root=arg.master,description="No max height or max width specified")
        return
    if(arg.val_ckbtn_maxheight.get() == 1):
        h = arg.ent_maxheight.get()
        if(not irutil.isnumber(h)):
            errorwindow.ErrorWindow(root=arg.master,description="Max height not a number")
            return
        args["maxheight"] = int(h)
    if(arg.val_ckbtn_maxwidth.get() == 1 ):
        w = arg.ent_maxwidth.get()
        if(not irutil.isnumber(w)):
            errorwindow.ErrorWindow(root=arg.master,description="Max width not a number")
            return
        args["maxwidth"]            = int(w)
    args["aspectratio"]         = (False,True)[arg.val_ckbtn_aspectratio.get() == 1]
    args["preserveextensions"]  = (False,True)[arg.cbfileextensions_preserve_val.get() == 1]
    args["multithreading"]      = (False,True)[arg.val_multithreading.get() == 1] 
    if(not args["preserveextensions"]):
        args["userextension"] = arg.rbfileextensions_val.get() 
        if(args["userextension"] == 'JPEG'):
            args["jpegquality"] = arg.val_jpegqualityslider.get()
    else:
        args["userextension"] = None
    fullpaths = []
    for i in arg.imglistselections:
        path = arg.filepath + arg.imgfilenames[i]
        fullpaths.append(path)
    ip.process(arg.master,arg.filepath,fullpaths,outfolder,args)
