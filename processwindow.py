import imgresize
import time
import _thread 
import tkinter as tk 
import PIL
import argprocessor
import threading
from tkinter import * 

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
        else:
            self.processwindow= tk.Toplevel(root)
            #self.processwindow.geometry(str(self.width) + "x" + str(self.height))
        self.processedfiles = 0 
        #self.master.title("Converting images")
        self.window_layout()
        self.processimages()

    def window_layout(self):
        self.processing = True
        self.processframe = tk.Frame(master=self.processwindow,width=640,height=30)
        self.processframe.grid(row=0,column=0,columnspan=10,rowspan=3)
        self.processindicators = []
        self.label_process = Label(master=self.processframe,text="Converting images")
        self.label_process.grid(row=0,column=3,columnspan=5)
        self.label_processedimg = Label(master=self.processframe,text="SomeCurrentImage.jpg",font="TkDefaultFont 10 bold",relief=GROOVE)
        self.label_processedimg.grid(row=2,column=0,columnspan=6,sticky="w")
        self.btn_quit = Button(master=self.processframe, text="Cancel",command=self.cancelordone)
        self.btn_quit.grid(row=2,column=7,columnspan=3,sticky="e",pady=5)
        for i in range(10):
            self.processindicators.append(tk.Canvas(master=self.processframe,border=3,relief=GROOVE,height=25,width=25,bg="red"))
            self.processindicators[i].grid(row=1,column=i)
        #DEBUGGING
        #_thread.start_new_thread(self.threadtest,(self.processindicators,1,))
        #_thread.start_new_thread(self.conversionlblanimation,(self.label_process,))

    def processimages(self):
        if(len(self.args) < 10):
            self.indicatorthreshold = 1
        else:
            self.indicatorthreshold = len(self.args) / 10
        obj = imgresize.IMGResize(self.args,self.multithreading,self.indicatorthreshold,self.processindicators).start()
        self.processwindow.after(100,self.testy)

    def testy(self):
        print("TESTINNNGGG")

    def cancelordone(self):
        if(self.processing):
            exit()
        else:
            exit()#TODO do i need to cancel threads 
    
    def conversionlblanimation(self,lbl):
        dotcount = 0
        convtxt = "Converting images"
        while(self.processing):
            lbl.config(text=convtxt)
            dotcount+=1
            convtxt += "."
            if(dotcount > 3):
                convtxt = "Converting images"
                dotcount = 0
            time.sleep(1)

    
    def threadtest(self,ind,sec):
        for j in range(len(ind)):
            time.sleep(sec)
            ind[j].config(bg="green")
        self.processing = False
    


if(__name__=="__main__"):
    top = Tk()
    process = ProcessWindow(top,None,10,None,debug=True)
    top.mainloop()
