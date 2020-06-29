import tkinter as tk

class ErrorWindow:
    def __init__(self,root,title="Error",height=10,width=15,message="Error occured"):
        self.errwindow = tk.Toplevel(root)
        self.title      = title
        self.win_height = height
        self.win_width  = width
        self.message    = message
        self.errwindow.title(self.title)
