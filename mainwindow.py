#!usr/bin/python3
import argprocessor as ip
import irutil 
import oututil
import mainargparser
from datetime import datetime,date,time
import errorwindow 
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
        self.ilheight   = 16
        self.noilheight = 5
        self.ilwidth    = 40
        self.outputpath = None
        self.imglistselections = []
        self.cbfileextensions_preserve_val  = IntVar()
        self.rbfileextensions_val           = StringVar()
        self.subfoldervar                   = IntVar() 
        self.filepath                       = None
        self.val_ckbtn_aspectratio          = IntVar()
        self.val_ckbtn_maxheight            = IntVar()
        self.val_multithreading             = IntVar()
        self.val_ckbtn_maxwidth             = IntVar()
        self.val_jpegqualityslider          = IntVar()
        
        self.selectfolderframe      = Frame(master=self,border=1,relief=GROOVE)
        self.outputfolderframe      = Frame(master=self,border=1,relief=GROOVE)
        self.qualityframe           = Frame(master=self,border=1,relief=GROOVE)
        self.extensionsframe        = Frame(master=self,border=1,relief=GROOVE)
        self.imagesizeoptionsframe  = Frame(master=self,border=1,relief=GROOVE)
        self.imgtextframe           = Frame(master=self,border=1,relief=GROOVE)
        self.extensionsframe        = Frame(master=self,border=1,relief=GROOVE)
        self.quitbtnframe           = Frame(master=self,border=1,relief=GROOVE)

        self.imgtextframe.grid(row=0,column=1,rowspan=15, columnspan=15,sticky="nse")
        self.selectfolderframe.grid(row=0,column=0,rowspan=2,sticky="nswe")
        self.outputfolderframe.grid(row=2,column=0,rowspan=2,sticky="nswe")
        self.qualityframe.grid(row=4,column=0,rowspan=3,sticky="nwse")
        self.extensionsframe.grid(row=7,column=0,rowspan=4,sticky="nwse")
        self.imagesizeoptionsframe.grid(row=11,column=0, rowspan=6,columnspan=16,sticky="nwse")
        self.quitbtnframe.grid(row=16,column=0)

        self.pack(fill=BOTH,expand=1)
        self.layout_imglistbox()
        self.layout_noimglistbox()
        self.layout_fileselection()
        self.layout_outputfolderselection()
        self.layout_qualityslider()
        self.layout_imagesizeoptions()
        self.layout_startconversion()
        self.cb_fileextensions_preserve()
        self.rb_fileextensions()
        self.imglist.bind("<<ListboxSelect>>", self.imgselection)

        self.quitButton = Button(master=self,text="Quit",command=self.quitprogram,height=1)
        self.quitButton.grid(row=16,column=15,sticky="e",pady=1)

        self.start_disableoptions() 

    def layout_noimglistbox(self):
        self.nonimglist = Listbox(master=self.imgtextframe,height = self.noilheight, width=self.ilwidth)
        self.nonimglistscrollbar = Scrollbar(master=self.imgtextframe, orient=VERTICAL)
        self.nonimglist.config(yscrollcommand=self.nonimglistscrollbar.set)
        self.nonimglistscrollbar.config(command=self.nonimglist.yview)
        self.nonimglistscrollbar.grid(row=6,column=14,sticky="nse")
        self.nonimglist.grid(row=6,column=0,columnspan=15)
        self.noimglabel = Label(master=self.imgtextframe, text="Not supported files",font="TkDefaultFont 10 bold")
        self.noimglabel.grid(row=5,column=1)

    def layout_outputfolderselection(self):
        self.lbl_output = Label(master=self.imgtextframe, text="Output:",font="TkDefaultFont 10 bold")
        self.lbl_outputpath = Label(master=self.imgtextframe)
        self.ckbtn_outputfolder = Button(master=self.outputfolderframe,text="Output folder",command=self.outputfolder)
        self.ckbtn_outputfolder.place(relx=0.15,rely=0.2)
        
        self.lbl_output.grid(row=1,column=0,sticky="w")
        self.lbl_outputpath.grid(row=1,column=1,sticky="w",columnspan=20)

    def layout_fileselection(self):
        self.ckbtn_filebtn      =Button(master=self.selectfolderframe,text="Input folder",command=self.selectfolder)
        self.ckbtn_subfolders   =Checkbutton(master=self.selectfolderframe,text="Subfolders",variable=self.subfoldervar).grid(row=1,column=0)
        self.dg_selectallbtn    =Button(master=self.imgtextframe, text="Select all",command=self.selectallimgs,bg="white")
        self.dg_selectallbtn.grid(row=2,column=14, sticky="e")
        self.ckbtn_filebtn.grid(row=0,column=0,padx=30,sticky="n",pady=self.bpad) 
        
    def layout_imagesizeoptions(self):
        self.header                         =Label(master=self.imagesizeoptionsframe, text="Image size options", font="TkDefaultFont 10 bold")
        self.ckbtn_preserve_aspectratio     =Checkbutton(master=self.imagesizeoptionsframe, text="Keep aspect ratio",command=self.aspectratio_check,variable=self.val_ckbtn_aspectratio)
        self.ckbtn_maxheight                =Checkbutton(master=self.imagesizeoptionsframe, text="Max height",variable=self.val_ckbtn_maxheight)
        self.ckbtn_maxwidth                 =Checkbutton(master=self.imagesizeoptionsframe, text="Max width",variable=self.val_ckbtn_maxwidth)
        self.ckbtn_multithreading           =Checkbutton(master=self.imagesizeoptionsframe, text="Multithreading",variable=self.val_multithreading)
        self.ent_maxheight                  =Entry(master=self.imagesizeoptionsframe,width=5)
        self.ent_maxwidth                   =Entry(master=self.imagesizeoptionsframe,width=5)
        self.lbl_ratioandor                 =Label(master=self.imagesizeoptionsframe,text="AND")
        
        self.header.grid(row=10,column=0, sticky="n", columnspan=2)
        self.lbl_ratioandor.grid(row=13,column=0,sticky="n",padx=30)
        self.ckbtn_maxheight.grid(row=12,column=0,sticky="w")
        self.ckbtn_maxwidth.grid(row=14,column=0,sticky="w")
        self.ent_maxheight.place(relx=0.22,rely=0.26)
        self.ent_maxwidth.place(relx=0.22,rely=0.52)
        self.ckbtn_preserve_aspectratio.grid(row=11,column=0,sticky="nw",columnspan=2) 
        self.ckbtn_multithreading.grid(row=15,column=0,sticky="nw")

    def aspectratio_check(self):
        if(self.val_ckbtn_aspectratio.get() == 1):
            self.lbl_ratioandor["text"] = "OR"
        else:
            self.lbl_ratioandor["text"] = "AND"

    def layout_startconversion(self):
        self.btn_startconversion = Button(master=self.imagesizeoptionsframe, text="Convert",command=self.process).grid(row=16,column=0,sticky="nw")

    def process(self):
        mainargparser.startconversion(self)

    def rb_fileextensions(self):
        MODES = [("JPEG","JPEG"),
                ("GIF","GIF"),
                ("PNG","PNG"),
                ("TIFF","TIFF"),
                ("BMP","BMP"),
                ("PPM","PPM")]
        extensions = ["JPEG","GIF","PNG","TIFF","BMP","ICO","PPM"]
        self.rbextensions = []
        currow=6
        curcol=0
        x_pos = 20
        y_pos = 30
        #make buttons for available extensions
        for text,mode in MODES:
            self.rbextensions.append(Radiobutton(master=self.extensionsframe,text=text,variable=self.rbfileextensions_val,value=mode))
        for j in range(len(self.rbextensions)):
            self.rbextensions[j].grid(row=currow,column=curcol,sticky="w")
            if(j%2==0 and j > 0):
                y_pos = y_pos + 20
                x_pos = 20
                self.rbextensions[j].place(x=x_pos,y=y_pos)
                x_pos = 90
            elif(j==0):
                self.rbextensions[j].place(x=x_pos,y=y_pos)
                x_pos = 90
            else:
                self.rbextensions[j].place(x=x_pos,y=y_pos)

    def cb_fileextensions_preserve(self):
        self.ckbtn_fileextensions = Checkbutton(master=self.extensionsframe, text="Original extensions",variable=self.cbfileextensions_preserve_val,command=self.file_extensionsuseroption)
        self.ckbtn_fileextensions.grid(row=8,column=0,sticky="e")

    def layout_qualityslider(self):
        self.qualityscalelabel = Label(master=self.qualityframe, text="JPEG Quality", font="TkDefaultFont 10 bold").grid(row=3,column=0,sticky="n")
        self.imgqualityslider = Scale(master=self.qualityframe, from_=0, to_=100,orient=HORIZONTAL,variable=self.val_jpegqualityslider)
        self.imgqualityslider.grid(row=5,column=0,padx=30,sticky="n")
        self.imgqualityslider.set(90)

    def layout_imglistbox(self):
        self.lbl_inputpathlbl = Label(master=self.imgtextframe,text="Input path:",font="TkDefaultFont 10 bold")
        self.lbl_inputpath = Label(master=self.imgtextframe)
        self.lbl_inputpathlbl.grid(row=0,column=0,sticky="w")
        self.lbl_inputpath.grid(row=0,column=1,sticky="w",columnspan=30)
        self.imglist = Listbox(master=self.imgtextframe,height = self.ilheight, width=self.ilwidth,selectmode=EXTENDED)
        self.imglistscrollbar = Scrollbar(master=self.imgtextframe, orient=VERTICAL)
        self.imglist.config(yscrollcommand=self.imglistscrollbar.set)
        self.imglistscrollbar.config(command=self.imglist.yview)
        self.imglistscrollbar.grid(row=3,column=14,sticky="nse")
        self.imglist.grid(row=3,column=0,columnspan=15)
        self.imglabel = Label(master=self.imgtextframe, text="Images",font="TkDefaultFont 10 bold")
        self.imglabel.grid(row=2,column=1,sticky="s") 

    def imgselection(self,event):
        self.imglistselections = event.widget.curselection()

    def selectallimgs(self):
        self.imglist.select_set(0,END)
        self.imglist.event_generate("<<ListboxSelect>>")

    def readfiles(self):
        if(self.subfoldervar.get() == 1):
            self.imgfilenames,self.nonimgfiles = irutil.getfiles(self.filepath,subfolders=True)
        else:
            self.imgfilenames,self.nonimgfiles = irutil.getfiles(self.filepath,subfolders=False)
        if(self.imglist.size() > 0 or self.nonimglist.size() > 0):
            self.imglist.delete(0,END)
            self.nonimglist.delete(0,END)
        for i in range(len(self.imgfilenames)):
            self.imglist.insert(END,self.imgfilenames[i])
        for j in range(len(self.nonimgfiles)):
            self.nonimglist.insert(END,self.nonimgfiles[j])
        if(self.imglist.size() < 1 ):
            self.dg_selectallbtn.config(state="disabled")
        else:
            self.dg_selectallbtn.config(state="normal")

    def quitprogram(self):
        exit()
    
    def outputfolder(self):
        self.outputpath = filedialog.askdirectory(initialdir=self.cacheddir)
        if(self.outputpath and self.outputpath != "" and self.outputpath is not None):
            p = self.outputpath
            if(len(p) > 35):
                p = p[0:32] + "..."
            self.lbl_outputpath.config(text=p)

    def selectfolder(self):
        temppath = filedialog.askdirectory(initialdir=self.cacheddir)
        if(temppath and temppath != ""):
            self.filepath = temppath
            self.cacheddir = self.filepath
            p = temppath
            if(len(p) > 35):
                p = p[0:32] + "..."
            self.lbl_inputpath.config(text=p)
            if(self.filepath and self.filepath != ""):
                self.readfiles()

    def start_disableoptions(self):
        self.dg_selectallbtn.config(state="disabled")
        for rbutton in self.rbextensions:
            rbutton.configure(state="disabled",tristatevalue = 0)
        self.ckbtn_fileextensions.select()

    def file_extensionsuseroption(self):
        if(self.cbfileextensions_preserve_val.get() == 1):
            for rbutton in self.rbextensions:
                rbutton.configure(state="disabled")
        else:
            for rbutton in self.rbextensions:
                rbutton.configure(state="normal")

if(__name__ == "__main__"):
    root = Tk()
    root.geometry("640x480")
    imgrsz = MainWindow(root)
    root.mainloop()
