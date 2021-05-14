import tkinter as tk

class ErrorWindow:
    def __init__(self,root,title="Error",height=100,width=150,message="Error occured"):
        self.errwindow = tk.Toplevel(root)
        self.title      = title
        self.win_height = height
        self.win_width  = width
        self.message    = message
        self.errwindow.title(self.title)
