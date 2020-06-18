from PIL import Image


class Resize_options:
    def __init__ (self,aspectratio=0,target_size=(),ogsize=(),extension=None,outputpath=None,multithreading=False):
        self.aspectratio= aspectratio
        self.target_size= target_size 
        self.extension  = extension
        self.outputpath = outputpath
        self.ogsize     = ogsize
        self.multithreading = multithreading 

def process(filepath,imgpaths,maxheight=-1,maxwidth=-1,preserveextensions=True,userextension=None,aspectratio=True,multithreading=False):
    args = Resize_options()
    args.multithreading = multithreading
    image_height = image_width = 0.0
    val_aspectratio = 0.0
    for i in range(len(imgpaths)):
        image = Image.open(imgpaths[i])
        target_height = target_width = 0
        image_width, image_height = image.size
        currentformat = (image.format,userextension)[preserveextensions]
        if(not maxheight == -1 and maxheight <= image_height):
            target_height = maxheight
        elif(not maxheight == - 1 and maxheight>image_height):
            target_height = image_height
        else:
            target_height = 0 
        if (not maxwidth == -1 and maxwidth <= image_width):
            target_width = maxwidth
        elif(not maxwidth == -1 and maxwidth>image_width):
            target_width = image_width    
        else:
            target_width = 0 
        args.target_size = target_width,target_height
        if(aspectratio):
            args.aspectratio = image_width / image_height
                
        if(not preserveextensions):
            args.extension = userextension
        else:
            args.extension = image.format
        print(f"imagepath{imgpaths[i]}")
        print(f"originalsize{image.size}")
        print(f"targetsize :{args.target_size}")
        print(f"aspectratio:{args.aspectratio}")
        print(f"extension:{args.extension}\n")
