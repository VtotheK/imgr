import time
import _thread 
import tkinter as tk 
from tkinter import * 

class ProcessWindow(Frame):
    def __init__(self,root,title,filecount,width,height,debug=False):
       #TODO REMOVE THIS PART
        if(debug):
            self.processwindow = Frame.__init__(self,root)
            self.master = root 
        else:
            self.processwindow= tk.Toplevel(root)
        self.width = width
        self.height = height
        self.filecount = filecount
        self.processedfiles = 0 
        self.master.title("KURWA")
        #self.processwindow.geometry(str(self.width) + "x" + str(self.height))
        self.createwindow()
    
    def createwindow(self):
        self.processframe = tk.Frame(master=self.processwindow,width=640,height=30,bg="blue")
        self.processframe.grid(row=1,column=0,columnspan=10,rowspan=2)
        self.processindicators = []
        for i in range(10):
            #ind = tk.Canvas(master=self.processframe,border=1,relief=GROOVE,height=10,width=10,bg="red").grid(row=1,column=i)
            self.processindicators.append(tk.Canvas(master=self.processframe,border=1,relief=GROOVE,height=20,width=20,bg="red"))
            self.processindicators[i].grid(row=1,column=i)
        _thread.start_new_thread(self.threadtest,(self.processindicators,1,))
    def threadtest(self,ind,sec):
        for j in range(len(ind)):
            time.sleep(sec)
            ind[j].config(bg="green")
    


if(__name__=="__main__"):
    top = Tk()
    process = ProcessWindow(root=top,title="Is this working",filecount=10,width=650,height=200,debug=True)
    top.mainloop()
