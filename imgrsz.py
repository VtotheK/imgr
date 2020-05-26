#!usr/bin/python3
import irutil 
from tkinter import *
from tkinter import filedialog

class MainWindow(Frame):
    
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.master = master
        print("Hello from constructor")
        self.window_layout()
    
    def window_layout(self):
        self.master.title="Kurwa App"
        self.filepath = StringVar()
        self.pack(fill=BOTH,expand=1)
        
        self.nonimglist = Listbox(master=self, height = 20, width=30)
        self.nonimglistscrollbar = Scrollbar(master=self, orient=VERTICAL)
        self.nonimglist.config(yscrollcommand=self.nonimglistscrollbar.set)
        self.nonimglistscrollbar.config(command=self.nonimglist.yview)
        self.nonimglistscrollbar.grid(row=3,column=3,sticky="nse")
        
        self.imglist = Listbox(master=self,height = 10, width=30)
        self.imglistscrollbar = Scrollbar(master=self, orient=VERTICAL)
        self.imglist.config(yscrollcommand=self.imglistscrollbar.set)
        self.imglistscrollbar.config(command=self.imglist.yview)
        self.imglistscrollbar.grid(row=2,column=2,sticky="nse")
        
        filebtn = Button(self,text="Select folder",command=self.selectfolder)
        quitButton = Button(master=self,text="Quit",command=self.quitprogram)
        quitButton.grid(row=1, column=1)
        
        self.imglist.grid(row=2,column=2)
        self.nonimglist.grid(row=3,column=3)
        #btn_readfiles = Button(self,text="Read files",command=self.readfiles)
        #btn_readfiles.grid(row=1,column=0)
        filebtn.grid(row=1,column=1)
    
    def readfiles(self):
        imgfiles,nonimgfiles = irutil.getfiles(self.filepath)
        if(self.imglist.size() > 0):
            self.imglist.delete(0,END)
        for i in range(len(imgfiles)):
            self.imglist.insert(END,imgfiles[i])
        for j in range(len(nonimgfiles)):
            self.nonimglist.insert(END,nonimgfiles[j])

    def quitprogram(self):
        exit()

    def selectfolder(self):
        self.filepath= filedialog.askdirectory(initialdir="/")
        self.readfiles()

if(__name__ == "__main__"):
    root = Tk()
    root.geometry("640x480")

    imgrsz = MainWindow(root)
    root.mainloop()
