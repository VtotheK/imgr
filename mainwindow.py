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
        self.lbxpad     = 10
        self.lbypad     = 20
        self.bpad       = 10
        self.ilheight   = 10
        self.ilwidth    = 30
        self.imgtextframe = Frame(master=self,border=1,relief=GROOVE)
        self.imgtextframe.grid(row=0,column=15,rowspan=15, columnspan=15,sticky="nse")
        self.optionframe = Frame(master=self,border=1,relief=GROOVE)
        self.optionframe.grid(row=0,column=0,rowspan=15, columnspan=15,sticky="ns")
        self.master.title="Kurwa App"
        self.filepath = StringVar()
        self.pack(fill=BOTH,expand=1)
        self.imglistbox()
        self.noimglistbox()
        self.selectallbutton()
        self.sliders()
        self.imglist.bind("<<ListboxSelect>>", self.imgselection)
        self.filebtn = Button(master=self.optionframe,text="Select folder",command=self.selectfolder)
        quitButton = Button(master=self,text="Quit",command=self.quitprogram,height=1)
        quitButton.grid(row=15,column=29,sticky="ne",pady=self.bpad)
        self.filebtn.grid(row=0,column=0,padx=self.bpad,sticky="n") 
    
    def noimglistbox(self):
        self.nonimglist = Listbox(master=self.imgtextframe,height = self.ilheight, width=self.ilwidth)
        self.nonimglistscrollbar = Scrollbar(master=self.imgtextframe, orient=VERTICAL)
        self.nonimglist.config(yscrollcommand=self.nonimglistscrollbar.set)
        self.nonimglistscrollbar.config(command=self.nonimglist.yview)
        self.nonimglistscrollbar.grid(row=3,column=1,sticky="nse")
        self.nonimglist.grid(row=3,column=1,padx = self.lbxpad)
        self.noimglabel = Label(master=self.imgtextframe, text="Not image files").grid(row=2,column=1,sticky="n")
    
    def sliders(self):
        self.qualityscalelabel = Label(master=self.optionframe, text="Quality").grid(row=3,column=0,sticky="n")
        self.imgqualityslider = Scale(master=self.optionframe, from_=0, to_=10,orient=HORIZONTAL)
        self.imgqualityslider.grid(row=4,column=0,sticky="n")

    def imglistbox(self):
        self.imglist = Listbox(master=self.imgtextframe,height = self.ilheight, width=self.ilwidth,selectmode=EXTENDED)
        self.imglistscrollbar = Scrollbar(master=self.imgtextframe, orient=VERTICAL)
        self.imglist.config(yscrollcommand=self.imglistscrollbar.set)
        self.imglistscrollbar.config(command=self.imglist.yview)
        self.imglistscrollbar.grid(row=1,column=1,sticky="nse")
        self.imglist.grid(row=1,column=1)
        self.imglabel = Label(master=self.imgtextframe, text="Images").grid(row=0,column=1,sticky="n") 
    
    def imgselection(self,event):
        self.imglistselections = event.widget.curselection()

    def selectallimgs(self):
        self.imglist.select_set(0,END)

    def readfiles(self):
        imgfilenames,nonimgfiles,imgfiles = irutil.getfiles(self.filepath)
        if(self.imglist.size() > 0):
            self.imglist.delete(0,END)
        for i in range(len(imgfiles)):
            self.imglist.insert(END,imgfilenames[i])
        for j in range(len(nonimgfiles)):
            self.nonimglist.insert(END,nonimgfiles[j])
        if(self.imglist.size() < 1 ):
            self.selectallbtn.config(state="disabled")
        else:
            self.selectallbtn.config(state="normal")
        
    def selectallbutton(self):
        self.selectallbtn= Button(master=self.imgtextframe, text="Select all",command=self.selectallimgs)
        self.selectallbtn.grid(row=2,column=1, sticky="n")

    def quitprogram(self):
        exit()

    def selectfolder(self):
        self.filepath= filedialog.askdirectory(initialdir="/")
        self.readfiles()
    
    def startdisableoptions(self):
        self.selectallbtn.config(state="disabled")
        
if(__name__ == "__main__"):
    root = Tk()
    root.geometry("640x480")
    imgrsz = MainWindow(root)
    root.mainloop()
