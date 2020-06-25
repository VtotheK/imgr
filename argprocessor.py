from PIL import Image


class Resize_options:
    def __init__ (self,aspectratio=0,target_size=(),ogsize=(),extension=None,outputpath=None,multithreading=False):
        self.aspectratio= aspectratio
        self.target_size= target_size 
        self.extension  = extension
        self.outputpath = outputpath
        self.ogsize     = ogsize
        self.multithreading = multithreading 

def process(filepath,imgpaths,outputpath,maxheight,maxwidth,preserveextensions=True,userextension=None,aspectratio=True,multithreading=False):
    print(f"MH:{maxheight} MW:{maxwidth}")
    args = Resize_options()
    args.multithreading = multithreading
    image_height = image_width = 0.0
    val_aspectratio = 0.0
    for i in range(len(imgpaths)):
        image = Image.open(imgpaths[i])
        target_height = target_width = 0
        image_width, image_height = image.size
        args.extension = (userextension,image.format)[preserveextensions]
        print(f"preserveextensions {preserveextensions}")
        if(not aspectratio):
            if(maxheight > 0 and maxheight<=image_height):
                target_height = maxheight
            elif(maxheight > 0 and maxheight>image_height):
                target_height = image_height
            else:
                target_height = image_height#TODO THIS SECTION STINKS
            if (maxwidth > 0 and maxwidth<=image_width):
                target_width = maxwidth
            elif(maxwidth > 0 and maxwidth>image_width):
                target_width = image_width    
            else:
                target_width = image_width
        args.target_size = target_width,target_height
        args.aspectratio = (image_width / image_height,target_width/target_height)[aspectratio]
         
        print(f"imagepath{imgpaths[i]}")
        print(f"originalsize{image.size}")
        print(f"targetsize :{args.target_size}")
        print(f"aspectratio:{args.aspectratio}")
        print(f"extension:{args.extension}\n")
