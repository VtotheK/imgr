import imgresize
import time
import _thread 
import tkinter as tk 
import PIL
import argprocessor
import threading
from tkinter import * 
from collections import deque

class ProcessWindow(Frame):
    def __init__(self,root,args,multithreading=False,debug=False):
       #TODO REMOVE THIS PART
        self.multithreading = multithreading
        self.processing = False
        self.args = args
        self.idicatorthreshold = 1
        if(debug):
            self.processwindow = Frame.__init__(self,root)
            self.master = root 
            self.window_layout()
        else:
            self.processwindow= tk.Toplevel(root)
            #self.processwindow.geometry(str(self.width) + "x" + str(self.height))
            self.processedfiles = 0 
            self.window_layout()
            self.processimages()
        #self.master.title("Converting images")

    def window_layout(self):
        self.processing = True
        self.processframe = tk.Frame(master=self.processwindow)
        self.processframe.grid(row=0,column=0,columnspan=10,rowspan=2)
        self.imagetextframe = tk.Frame(master=self.processwindow,border=1)
        self.imagetextframe.grid(row=2,column=0,columnspan=10,rowspan=3)
        self.processindicators = deque() 
        self.label_process = Label(master=self.processframe,text="Converting images")
        self.label_process.grid(row=1,column=3,columnspan=5)
        self.label_rsztext = Label(master=self.imagetextframe,text="Resizing:")
        self.label_rsztext.grid(row=3,column=0,sticky="w",columnspan=1)
        self.label_processedimg = Label(master=self.imagetextframe,text="SomeCurrentImage.jpg",font="TkDefaultFont 10 bold",relief=GROOVE,height=1,width=20)
        self.label_processedimg.grid(row=3,column=1,sticky="w")
        self.btn_quit = Button(master=self.imagetextframe, text="Cancel",command=self.cancelordone)
        self.btn_quit.grid(row=3,column=7,columnspan=3,sticky="e",pady=5)
        for i in range(10):
            self.processindicators.append(tk.Canvas(master=self.processframe,border=3,relief=GROOVE,height=25,width=25,bg="red"))
            self.processindicators[i].grid(row=1,column=i)
        #DEBUGGING
        #_thread.start_new_thread(self.threadtest,(self.processindicators,1,))
        #_thread.start_new_thread(self.conv_animation,(self.label_process,))
    
    def resizedone(self):
        self.processing = False
    
    def currentlyresizing(self,path):
        self.label_processedimg.config(text=path)

    def processimages(self):
        if(len(self.args) < 10):
            self.indicatorthreshold = 1
        else:
            self.indicatorthreshold = len(self.args) / 10
        obj = imgresize.IMGResize(self,self.args,self.multithreading,self.indicatorthreshold,self.processindicators).start()
        _thread.start_new_thread(self.conv_animation,())
    def testy(self):
        print("TESTINNNGGG")

    def cancelordone(self):
        if(self.processing):
            exit()
        else:
            exit()#TODO do i need to cancel threads 
    
    def conv_animation(self):
        dotcount = 0
        convtxt = "Converting images"
        while(self.processing):
            self.label_process.config(text=convtxt)
            dotcount+=1
            convtxt += "."
            if(dotcount > 3):
                convtxt = "Converting images"
                dotcount = 0
            time.sleep(1)
        self.label_process.config(text="Conversion done")

    
    def threadtest(self,ind,sec):
        for j in range(len(ind)):
            time.sleep(sec)
            ind[j].config(bg="green")
        self.processing = False
    


if(__name__=="__main__"):
    top = Tk()
    process = ProcessWindow(top,None,multithreading=False,debug=True)
    top.mainloop()
