import tkinter as tk 
from tkinter import * 

class ProcessWindow:
    def __init__(self,root,title,filecount,width,height):
        self.processwindow = tk.Toplevel(root)
        self.filecount = filecount
        self.width = width
        self.height = height
        self.createwindow()

    def createwindow(self):
        self.processwindow.geometry = (str(self.width) + "x" + str(self.height))
        self.lbl = Label(master=self.processwindow, text=str(self.filecount)).pack()
