import _thread
import threading
import time
import PIL
import os
from tkinter import * 
from PIL import Image
from collections import deque

imgxtensions = ["jpg","jpeg","gif","tiff","bmp",""]

def trimfilename(filename,ext):
    fsplit = filename.split(".")
    if(len(fsplit)>0):
        if(fsplit[-1] == ext.lower() or fsplit[-1] == "jpg"):
            print(f"{filename} had a file extension in it's name, erasing")
            filename = (str(time.time()),filename[0:len(filename) - len(fsplit[-1]) - 1])[len(filename) - len(fsplit) > 0] #after 6 months of writing this, i have no clue what this line does. Note to self, don't go egotripping when writing code. 
    return filename

class IMGResize(threading.Thread):
    def __init__(self,sender,args,multithreading,indicatorthreshold,processindicators):
        threading.Thread.__init__(self)
        self.sender = sender
        self.cresized = 0
        self.indicatorthreshold = indicatorthreshold
        self.processindicators = processindicators
        self.args = args
        self.multithreading = multithreading
        self.indicatorthreshold = indicatorthreshold
        self.processindicators = processindicators 
        self.resized_amount = 0

    def run(self):
        print(f"Active threads:{threading.activeCount()}")
        time.sleep(3)
        self.currentthreads = []
        allthreads = []
        max_threads = 5
        start_time = time.time()
        if(self.multithreading):
            while(len(self.args) > 0):
                if(len(self.currentthreads) < max_threads):
                    for i in range(max_threads - threading.activeCount()):
                        if(len(self.args) > 0):
                            try:
                                arg = self.args.pop()
                            except IndexError:
                                print("Tried to pop image from empty arg-queue")
                                return False
                            thread = threading.Thread(target=self.resize, args=(arg,True))
                            thread.start()
                            print("THREAD SPAWNED")
                            allthreads.append(thread)
                        else:
                            for i in range(len(allthreads)):
                                allthreads[i].join
                                print(f("THREAD:{allthreads[i]} joined"))
                else:
                    print("RESIZE MAIN-THREAD SLEEPING")
                    time.sleep(0.4)
            for i in range(len(allthreads)):
                allthreads[i].join()
        else:
            for i in range(len(self.args)):
                arg = self.args[i]
                self.resize(arg,False)
        if(len(self.processindicators) > 0):
            while(len(self.processindicators) > 0):
                self.processindicators.popleft().config(bg="green")
        self.sender.resizedone()
        end_time = time.time()
        print(f"Resized {self.resized_amount} image in {round(end_time-start_time,2)} seconds.")

    def resize(self,arg,multithreading):
        if(multithreading):
            tid = threading.get_ident()
            self.currentthreads.append(tid)
            print(f"THREAD:{threading.current_thread().ident} -> starting to work")
        try:
            self.sender.currentlyresizing(os.path.basename(arg.imgpath))
            img = Image.open(arg.imgpath) 
            filename = trimfilename(os.path.basename(arg.imgpath),img.format)
            print(f"THREAD:{threading.current_thread().ident} -> Resizing:{arg.imgpath}")
            img = img.resize(arg.target_size,PIL.Image.LANCZOS)
            out = arg.outputpath + "/" + filename
            print(f"THREAD:{threading.current_thread().ident} -> Saving: {out}")
            if(arg.extension == 'JPEG'):
                jpegquality = arg.jpegquality
                filename = out + "." + str(arg.extension).lower()
                if(img.mode in("RGBA","P")):
                    rbg_img = img.convert("RGB")
                    rbg_img.save(filename,"JPEG",quality=jpegquality)
                else:
                    img.save(filename,'JPEG',quality=jpegquality)
            else:
                img.save(out + "." +str(arg.extension).lower(),arg.extension)
        except (OSError,KeyError,ValueError) as e: 
            print("Could not resize image file, unsupported file type")
        finally:
            self.cresized = self.cresized + 1
            self.resized_amount = self.resized_amount + 1
            if(self.cresized > self.indicatorthreshold):
                try:
                    ind = self.processindicators.popleft()
                    ind.config(bg="green")
                    self.cresized = 0
                except IndexError:
                    print("Tried to pop from empty queue")
        print(f"THREAD:{threading.current_thread().ident} -> Image resized")
        if(multithreading):
            print(f"THREAD:{threading.current_thread().ident} -> stopping")
            tid = threading.get_ident()
            self.currentthreads.remove(tid)

