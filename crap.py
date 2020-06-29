
import threading
import tkinter as tk 
from tkinter import * 
class ProcessWindow(Frame):
    def __init__(self,root,title,filecount,width,height,debug=False):
        if(debug):
            self.crap = Frame.__init__(self,root)
            self.master = root 
            #self.pack()
        else:
            self.processwindow= tk.Toplevel(root)
        self.derp = Frame(master=self.crap, height=30,width=30,bg="blue")
        self.derp.grid(row=0,column=0)
        self.lbl = Label(master=self.derp,text="CUCKHOLDER").grid(row=0,column=0)
if(__name__=="__main__"):
    top = Tk()
    #top.geometry("520x482")
    #top.title("MainWindow")
    #imgrsz = mainwindow.MainWindow(root)
    process = ProcessWindow(root=top,title="Is this working",filecount=10,width=650,height=200,debug=True)
    top.mainloop()
