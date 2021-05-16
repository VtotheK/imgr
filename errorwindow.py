import tkinter as tk
from tkinter import * 

class ErrorWindow:
    def __init__(self,root,description,height=100,width=150,title="Error occured"):
        self.errwindow = tk.Toplevel(root)
        self.title      = title
        self.win_height = height
        self.win_width  = width
        self.description= description 
        self.errwindow.title(self.title)
        self.window_layout()

    def window_layout(self):
        lbl = Label(master=self.errwindow, text=self.description)
        lbl.pack()

