import threading
import PIL
from PIL import Image
from collections import deque

num = 1 #TODO change this to filename, remember all PIL.Image objects wont have filename property

def resizeimages(args,multithreading,indicatorthreshold,processindicators):
    print(f"THREADS:{threading.activeCount()}")
    currentthreads = []
    allthreads = []
    max_threads = 5
    if(multithreading):
        while(len(args) > 0):
            if(len(currentthreads) < max_threads):
                for i in range(max_threads - threading.activeCount()):
                    if(len(args) > 0):
                        try:
                            arg = args.pop()
                        except IndexError:
                            print("Tried to pop image from empty arg-queue")
                            return False #TODO handle this return somehow
                        thread = threading.Thread(target=resize, args=(arg,True))
                        allthreads.append(thread)
                    #else:
                      #  for i in range(len(allthreads)):
                       #     allthreads[i].join
            else:
                time.sleep(0.4)
        for i in range(len(allthreads)):
            allthreads[i].join()
    else:
        for i in range(len(args)):
            arg = args[i]
            resize(arg,False)

def resize(arg,multithreading):
   if(multithreading):
        tid = thread.get_ident()
        currentthreads.append(tid)
        print(f"THREAD:{threading.current_thread().ident} starting to work")
   img = Image.open(arg.imgpath)
   print(f"Resizing:{arg.imgpath}")
   img = img.resize(arg.target_size,PIL.Image.LANCZOS)
   global num  
   out = arg.outputpath + "/" + str(num)
   num = num + 1
   img.save(out,arg.extension)
   print("Image resized")
   if(multithreading):
        print(f"THREAD:{threading.current_thread().ident} stopping")
        tid = thread.get_ident()
        currentthreads.remove(tid)
