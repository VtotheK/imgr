#!usr/bin/python3

import tkinter as tk

mainwindow = tk.Tk()

rframe = tk.Frame(master=mainwindow, width=50, height=50, bg="red")
bframe = tk.Frame(master=mainwindow, width=25, height=25, bg="blue")
yframe = tk.Frame(master=mainwindow, width=75, height=75, bg="yellow")
btn = tk.Button(master=yframe,text="btntext")
yframe.pack()
rframe.pack()
btn.pack()
bframe.pack()
mainwindow.mainloop()
