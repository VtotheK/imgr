#!usr/bin/python3
import irutil 
from tkinter import *
from tkinter import filedialog

class MainWindow(Frame):
    
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.master = master
        self.window_layout()
    
    def window_layout(self):
        self.cacheddir  = "/"
        self.lbxpad     = 10
        self.lbypad     = 20
        self.bpad       = 10
        self.ilheight   = 10
        self.ilwidth    = 40
        self.imgtextframe = Frame(master=self,border=1,relief=GROOVE)
        self.imgtextframe.grid(row=0,column=15,rowspan=15, columnspan=15,sticky="nse")
        self.selectfolderframe = Frame(master=self,border=1,relief=GROOVE)
        self.selectfolderframe.grid(row=0,column=0,rowspan=2, columnspan=15,sticky="nswe")
       #self.optionframe = Frame(master=self, border=1, relief=GROOVE)
       #self.optionframe.grid(row=2,column=0,rowspan=13,columnspan=15,sticky="ns")
        self.qualityframe = Frame(master=self,border=1,relief=GROOVE)
        self.qualityframe.grid(row=2,column=0,rowspan=2,columnspan=15,sticky="nwse")
        self.extensionsframe = Frame(master=self,border=1,relief=GROOVE)
        self.extensionsframe.grid(row=4,column=0,rowspan=6,columnspan=15,sticky="nwse")
        self.master.title="Kurwa App"
        self.cbfileextensions_preserve_val = IntVar()
        self.rbfileextensions_val = IntVar()
        self.subfoldervar = IntVar() 
        self.filepath = StringVar()
        self.pack(fill=BOTH,expand=1)
        self.imglistbox()
        self.noimglistbox()
        self.selectallbutton()
        self.sliders()
        self.cbfileextensions_preserve()
        self.rbfileextensions()
        self.ckbtn_subfolders()
        self.imglist.bind("<<ListboxSelect>>", self.imgselection)
        self.filebtn = Button(master=self.selectfolderframe,text="Select folder",command=self.selectfolder)
        quitButton = Button(master=self,text="Quit",command=self.quitprogram,height=1)
        quitButton.grid(row=15,column=29,sticky="ne",pady=self.bpad)
        self.filebtn.grid(row=0,column=0,padx=30,sticky="n",pady=self.bpad) 
    
    def noimglistbox(self):
        self.nonimglist = Listbox(master=self.imgtextframe,height = self.ilheight, width=self.ilwidth)
        self.nonimglistscrollbar = Scrollbar(master=self.imgtextframe, orient=VERTICAL)
        self.nonimglist.config(yscrollcommand=self.nonimglistscrollbar.set)
        self.nonimglistscrollbar.config(command=self.nonimglist.yview)
        self.nonimglistscrollbar.grid(row=4,column=1,sticky="nse")
        self.nonimglist.grid(row=4,column=1,padx = self.lbxpad)
        self.noimglabel = Label(master=self.imgtextframe, text="Not supported files").grid(row=3,column=1,sticky="n")
   
    def ckbtn_subfolders(self):
        ckbtn = Checkbutton(master=self.selectfolderframe,text="Subfolders",variable=self.subfoldervar).grid(row=1,column=0)
    
    def rbfileextensions(self):
        Label(master=self.extensionsframe, text="Output file(s)").grid(row=5,column=0)
        MODES = [("JPEG","JPEG"),
                 ("GIF","GIF"),
                 ("PNG","PNG"),
                 ("TIFF","TIFF"),
                 ("BMP","BMP"),
                 ("ICO","ICO"),
                 ("PPM","PPM")]
        extensions = ["JPEG","GIF","PNG","TIFF","BMP","ICO","PPM"]
        self.rbextensions = []
        currow=6
        curcol=0
        x_place = 20
        y_place = 40
        for text,mode in MODES:
            self.rbextensions.append(Radiobutton(master=self.extensionsframe,text=text,variable=self.rbfileextensions_val,value=mode))
        for j in range(len(self.rbextensions)):
            self.rbextensions[j].grid(row=currow,column=curcol,sticky="w")
            if(j%2==0 and j > 0):
                y_place = y_place + 20
                x_place = 20
                self.rbextensions[j].place(x=x_place,y=y_place)
                x_place = 90
            elif(j==0):
                self.rbextensions[j].place(x=x_place,y=y_place)
                x_place = 90
            else:
                self.rbextensions[j].place(x=x_place,y=y_place)
         
    def cbfileextensions_preserve(self):
        self.fileextensions = Checkbutton(master=self.extensionsframe, text="Original extensions",variable=self.cbfileextensions_preserve_val)
        self.fileextensions.grid(row=7,column=0,sticky="e")

    def sliders(self):
        self.qualityscalelabel = Label(master=self.qualityframe, text="Quality").grid(row=3,column=0,sticky="n")
        self.imgqualityslider = Scale(master=self.qualityframe, from_=0, to_=10,orient=HORIZONTAL)
        self.imgqualityslider.grid(row=4,column=0,padx=30,sticky="n")

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
        if(self.subfoldervar.get() == 1):
            imgfilenames,nonimgfiles,imgfiles = irutil.getfiles(self.filepath,subfolders=True)
        else:
            imgfilenames,nonimgfiles,imgfiles = irutil.getfiles(self.filepath,subfolders=False)
        if(self.imglist.size() > 0 or self.nonimglist.size() > 0):
            self.imglist.delete(0,END)
            self.nonimglist.delete(0,END)
        for i in range(len(imgfiles)):
            self.imglist.insert(END,imgfilenames[i])
        for j in range(len(nonimgfiles)):
            self.nonimglist.insert(END,nonimgfiles[j])
        if(self.imglist.size() < 1 ):
            self.selectallbtn.config(state="disabled")
        else:
            self.selectallbtn.config(state="normal")
        
    def selectallbutton(self):
        self.selectallbtn= Button(master=self.imgtextframe, text="Select all",command=self.selectallimgs,bg="white")
        self.selectallbtn.grid(row=0,column=1, sticky="e")

    def quitprogram(self):
        exit()

    def selectfolder(self):
        self.filepath = filedialog.askdirectory(initialdir=self.cacheddir)
        self.cacheddir = self.filepath
        if(self.filepath):
            self.readfiles()

    def startdisableoptions(self):
        self.selectallbtn.config(state="disabled")
        
if(__name__ == "__main__"):
    root = Tk()
    root.geometry("640x480")
    imgrsz = MainWindow(root)
    root.mainloop()
