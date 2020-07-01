import threading
import PIL
from collections import deque

def resizeimages(args,multithreading,indicatorthreshold,processindicators):
    print(f"THREADS:{threading.activeCount()}")
    currentthread = []
    if(multithreading):
        while(len(args) > 0):
            if(len(currentthreads) < 10):
                for i in range(10 - threading.activeCount()):
                    try:
                        arg = args.pop()
                    except IndexError:
                        print("Tried to pop image from empty arg-queue")
                        return False
                    thread = threading.Thread(target=resize, args=(arg,))
                    currentthreads.add(thread.get_ident())
            else:
                time.sleep(0.4)
    else:
        while(len(args > 0):
            pass
        pass

def resize(arg):
   img = Image.open(arg.imgpath)
   img = img.resize(arg.size,PIL.Image.LANCZOS)
   out = arg.outputpath + "/" + img.filename
   img.save(out,arg.extension)
   tid = thread.get_ident()
   currentthreads.remove(tid)
