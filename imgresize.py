import _thread
import threading
import time
import PIL
import os
from tkinter import * 
from PIL import Image
from collections import deque


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

    def run(self):
        print(f"THREADS:{threading.activeCount()}")
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
                                return False #TODO handle this return somehow
                            thread = threading.Thread(target=self.resize, args=(arg,True))
                            thread.start()
                            #t = _thread.start_new_thread(self.resize,(arg,True,))
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
        print(f"Total time: {round(end_time-start_time,2)} seconds")

    def resize(self,arg,multithreading):

        if(multithreading):
            tid = threading.get_ident()
            self.currentthreads.append(tid)
            print(f"THREAD:{threading.current_thread().ident} -> starting to work")
        try:
            self.sender.currentlyresizing(arg.imgpath)
            img = Image.open(arg.imgpath) 
            ext = img.format
            filename = os.path.basename(arg.imgpath)
            fsplit = filename.split(".")
            if(len(fsplit)>0):
                if(fsplit[-1] == ext.lower()):
                    print(f"{filename} had a file extension in it's name, erasing")
                    filename = (str(time.time()),filename[0:len(filename) - len(fsplit[-1]) - 1])[len(filename) - len(fsplit) > 0]
                    
                    #filename = filename[0:len(filename) - len(fsplit)]
            print(f"THREAD:{threading.current_thread().ident} -> Resizing:{arg.imgpath}")
            img = img.resize(arg.target_size,PIL.Image.LANCZOS)
            out = arg.outputpath + "/" + filename
            print(f"THREAD:{threading.current_thread().ident} -> Saving: {out}")
            img.save(out,arg.extension)
        except (OSError,KeyError,ValueError) as e: #TODO too many exceptions, must parse input files more carefully, remove when implemented
            print("Could not resize image file, unsupported file type")
        finally:
            self.cresized = self.cresized + 1
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
