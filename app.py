import os 
import mainwindow
from tkinter import *

if(__name__=="__main__"):
    root = Tk()
    root.geometry("530x515")
    root.title("MainWindow")
    root.resizable(False,False)
    imgrsz = mainwindow.MainWindow(root)
    root.mainloop()
