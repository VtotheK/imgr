import _thread
import threading
import time
import PIL
from PIL import Image
from collections import deque

num = 1 #TODO change this to filename, remember all PIL.Image objects wont have filename property

class IMGResize(threading.Thread):
    def __init__(self,args,multithreading,indicatorthreshold,processindicators):
        threading.Thread.__init__(self)
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
                            #thread = threading.Thread(target=self.resize, args=(arg,True)).run()
                            t = _thread.start_new_thread(self.resize,(arg,True,))
                            print("THREAD APPENDING")
                            allthreads.append(t)
                        #else:
                          #  for i in range(len(allthreads)):
                           #     allthreads[i].join
                else:
                    time.sleep(0.4)
            #for i in range(len(allthreads)):
               # allthreads[i].join()
        else:
            for i in range(len(self.args)):
                arg = self.args[i]
                self.resize(arg,False)

    def resize(self,arg,multithreading):
       global num  
       if(multithreading):
            tid = threading.get_ident()
            self.currentthreads.append(tid)
            print(f"THREAD:{threading.current_thread().ident} starting to work")
       img = Image.open(arg.imgpath)
       print(f"Resizing:{arg.imgpath}")
       img = img.resize(arg.target_size,PIL.Image.LANCZOS)
       out = arg.outputpath + "/" + str(num)
       num = num + 1
       img.save(out,arg.extension)
       print("Image resized")
       if(multithreading):
            print(f"THREAD:{threading.current_thread().ident} stopping")
            tid = threading.get_ident()
            self.currentthreads.remove(tid)
