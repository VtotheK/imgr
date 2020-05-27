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
        pad = 20
        self.master.title="Kurwa App"
        self.filepath = StringVar()
        self.pack(fill=BOTH,expand=1)
        
        self.imglist = Listbox(master=self,height = 10, width=30)
        self.imglistscrollbar = Scrollbar(master=self, orient=VERTICAL)
        self.imglist.config(yscrollcommand=self.imglistscrollbar.set)
        self.imglistscrollbar.config(command=self.imglist.yview)
        self.imglistscrollbar.grid(row=1,column=2,sticky="nse",pady=pad,padx=pad)
        self.imglist.grid(row=1,column=2,pady=pad,padx=pad)
        self.imglabel = Label(master=self, text="Img").grid(row=1,column=2,sticky="n") 
        
        self.nonimglist = Listbox(master=self, height = 10, width=30)
        self.nonimglistscrollbar = Scrollbar(master=self, orient=VERTICAL)
        self.nonimglist.config(yscrollcommand=self.nonimglistscrollbar.set)
        self.nonimglistscrollbar.config(command=self.nonimglist.yview)
        self.nonimglistscrollbar.grid(row=2,column=2,sticky="nse",pady=pad,padx=pad)
        self.nonimglist.grid(row=2,column=2,pady=pad,padx=pad)
        self.noimglabel = Label(master=self, text="Not image files").grid(row=2,column=2,sticky="n")
        
        filebtn = Button(self,text="Select folder",command=self.selectfolder)
        quitButton = Button(master=self,text="Quit",command=self.quitprogram,height=1)
        quitButton.grid(row=2,column=2,sticky="se")
         
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
    root.geometry("840x680")

    imgrsz = MainWindow(root1
    root.mainloop()
