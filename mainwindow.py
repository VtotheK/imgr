#!usr/bin/python3
import irutil 
import oututil
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
        self.cbfileextensions_preserve_val  = IntVar()
        self.rbfileextensions_val           = IntVar()
        self.subfoldervar                   = IntVar() 
        self.filepath                       = StringVar()
        self.val_ckbtn_aspectratio          = IntVar()
        self.val_ckbtn_maxheight            = IntVar()
        self.val_ckbtn_maxwidth             = IntVar()
        self.selectfolderframe      = Frame(master=self,border=1,relief=GROOVE)
        self.qualityframe           = Frame(master=self,border=1,relief=GROOVE)
        self.extensionsframe        = Frame(master=self,border=1,relief=GROOVE)
        self.imagesizeoptionsframe  = Frame(master=self,border=1,relief=GROOVE)
        self.imgtextframe           = Frame(master=self,border=1,relief=GROOVE)
        self.extensionsframe        = Frame(master=self,border=1,relief=GROOVE)
         
        self.imgtextframe.grid(row=0,column=15,rowspan=15, columnspan=15,sticky="nse")
        self.selectfolderframe.grid(row=0,column=0,rowspan=2, columnspan=15,sticky="nswe")
        self.qualityframe.grid(row=2,column=0,rowspan=2,columnspan=15,sticky="nwse")
        self.extensionsframe.grid(row=4,column=0,rowspan=5,columnspan=15,sticky="nwse")
        self.imagesizeoptionsframe.grid(row=9,column=0, rowspan=6,columnspan=15,sticky="nwse")
        

        self.master.title="Kurwa App"
        self.pack(fill=BOTH,expand=1)
        self.layout_imglistbox()
        self.layout_noimglistbox()
        self.layout_fileselection()
        self.layout_qualityslider()
        self.layout_imagesizeoptions()
        self.layout_startconversion()
        self.cb_fileextensions_preserve()
        self.rb_fileextensions()
        self.imglist.bind("<<ListboxSelect>>", self.imgselection)
        
        quitButton = Button(master=self,text="Quit",command=self.quitprogram,height=1)
        quitButton.grid(row=15,column=29,sticky="ne")
        
        self.start_disableoptions() 
    
    def layout_noimglistbox(self):
        self.nonimglist = Listbox(master=self.imgtextframe,height = self.ilheight, width=self.ilwidth)
        self.nonimglistscrollbar = Scrollbar(master=self.imgtextframe, orient=VERTICAL)
        self.nonimglist.config(yscrollcommand=self.nonimglistscrollbar.set)
        self.nonimglistscrollbar.config(command=self.nonimglist.yview)
        self.nonimglistscrollbar.grid(row=4,column=1,sticky="nse")
        self.nonimglist.grid(row=4,column=1,padx = self.lbxpad)
        self.noimglabel = Label(master=self.imgtextframe, text="Not supported files").grid(row=3,column=1,sticky="n")
   
    def layout_fileselection(self):
        self.ckbtn_filebtn      =Button(master=self.selectfolderframe,text="Select folder",command=self.selectfolder)
        self.ckbtn_subfolders   =Checkbutton(master=self.selectfolderframe,text="Subfolders",variable=self.subfoldervar).grid(row=1,column=0)
        self.dg_selectallbtn    =Button(master=self.imgtextframe, text="Select all",command=self.selectallimgs,bg="white")
        self.dg_selectallbtn.grid(row=0,column=1, sticky="e")
        self.ckbtn_filebtn.grid(row=0,column=0,padx=30,sticky="n",pady=self.bpad) 
    
    def layout_imagesizeoptions(self):
        self.header                         =Label(master=self.imagesizeoptionsframe, text="Image size options", font="TkDefaultFont 10 bold")
        self.ckbtn_preserve_aspectratio     =Checkbutton(master=self.imagesizeoptionsframe, text="Keep aspect ratio",command=self.aspectratio_check,variable=self.val_ckbtn_aspectratio)
        self.ckbtn_maxheight                =Checkbutton(master=self.imagesizeoptionsframe, text="Max height",variable=self.val_ckbtn_maxheight)
        self.ckbtn_maxwidth                 =Checkbutton(master=self.imagesizeoptionsframe, text="Max width",variable=self.val_ckbtn_maxwidth)
        self.ent_maxheight                  =Entry(master=self.imagesizeoptionsframe,width=8)
        self.ent_maxwidth                   =Entry(master=self.imagesizeoptionsframe,width=8)
        self.lbl_ratioandor                 =Label(master=self.imagesizeoptionsframe,text="AND")
        self.header.grid(row=9,column=0, sticky="n", columnspan=2)
        self.lbl_ratioandor.grid(row=12,column=0,sticky="n",padx=30)
        self.ckbtn_maxheight.grid(row=11,column=0,sticky="w")
        self.ckbtn_maxwidth.grid(row=13,column=0,sticky="w")
        self.ent_maxheight.grid(row=13,column=1,sticky="s")
        self.ent_maxwidth.grid(row=11,column=1,sticky="s")
        self.ckbtn_preserve_aspectratio.grid(row=10,column=0,sticky="nw",columnspan=2) 

    def aspectratio_check(self):
        if(self.val_ckbtn_aspectratio.get() == 1):
            self.lbl_ratioandor["text"] = "OR"
        else:
            self.lbl_ratioandor["text"] = "AND"
    
    def layout_startconversion(self):
        self.btn_startconversion = Button(master=self, text="Convert").grid(row=15,column=0,sticky="nw")

    def rb_fileextensions(self):
        Label(master=self.extensionsframe, text="Output file(s)",font="TkDefaultFont 10 bold").grid(row=5,column=0)
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
         
    def cb_fileextensions_preserve(self):
        self.ckbtn_fileextensions = Checkbutton(master=self.extensionsframe, text="Original extensions",variable=self.cbfileextensions_preserve_val,command=self.file_extensionsuseroption)
        self.ckbtn_fileextensions.grid(row=7,column=0,sticky="e")

    def layout_qualityslider(self):
        self.qualityscalelabel = Label(master=self.qualityframe, text="JPEG Quality", font="TkDefaultFont 10 bold").grid(row=3,column=0,sticky="n")
        self.imgqualityslider = Scale(master=self.qualityframe, from_=0, to_=10,orient=HORIZONTAL)
        self.imgqualityslider.grid(row=4,column=0,padx=30,sticky="n")

    def layout_imglistbox(self):
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
            self.dg_selectallbtn.config(state="disabled")
        else:
            self.dg_selectallbtn.config(state="normal")
        
    def quitprogram(self):
        exit()

    def selectfolder(self):
        self.filepath = filedialog.askdirectory(initialdir=self.cacheddir)
        self.cacheddir = self.filepath
        if(self.filepath):
            self.readfiles()

    def start_disableoptions(self):
        self.dg_selectallbtn.config(state="disabled")
        for rbutton in self.rbextensions:
            rbutton.configure(state="disabled")
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
