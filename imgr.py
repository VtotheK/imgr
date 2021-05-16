import os 
import mainwindow
from tkinter import *
from PIL import Image, ImageTk

if(__name__=="__main__"):
    root = Tk()
    root.geometry("495x515")
    root.title("MainWindow")
    root.resizable(False,False)
    icon = Image.open("img/icon")
    bticon = ImageTk.PhotoImage(icon)
    root.wm_iconphoto(True,bticon)
    imgrsz = mainwindow.MainWindow(root)
    root.mainloop()
