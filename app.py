import os 
import mainwindow
from tkinter import *

if(__name__=="__main__"):
    root = Tk()
    root.geometry("515x495")
    root.title("MainWindow")
    imgrsz = mainwindow.MainWindow(root)
    root.mainloop()
