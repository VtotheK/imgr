import tkinter as tk
from tkinter import * 

class ErrorWindow:
    def __init__(self,root,description,title="Error"):
        self.errwindow = tk.Toplevel(root)
        self.title      = title
        self.description= description 
        self.errwindow.title(self.title)
        self.window_layout()

    def window_layout(self):
        lbl = Label(master=self.errwindow, text=self.description,width=20,height=10,font="Helvetica 12 bold",wraplength=150,justify=CENTER)
        lbl.pack()

