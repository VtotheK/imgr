from PIL import Image


class Resize_options:
    def __init__ (self,aspectratio=0,size=(),extension=None,outputpath=None):
        self.aspectratio= aspectratio
        self.size       = size 
        self.extension  = extension
        self.outputpath = outputpath


def process(filepath,imgpaths,maxheight=-1,maxwidth=-1,preserveextensions=True,userextension=None,aspectratio=True):
    args = Resize_options()
    target_height = target_width = 0
    image_height = image_width = 0.0
    val_aspectratio = 0.0
    for i in range(len(imgpaths)):
        image = Image.open(imgpaths[i])
        img_width, img_height = image.size
        currentformat = (image.format,userextension)[preserveextensions]
        if(not maxheight == -1 and maxheight <= image_height):
            target_height = maxheight
        else:
            target_height = -1  
        if (not maxwidth == -1 and maxwidth <= image_width):
            target_width = maxwidth
        else:
            target_width = -1 
        args.size = target_width,target_height
        
        if(aspectratio):
            args.aspectratio = img_width / img_height
        if(not preserveextensions):
            args.extension = userextension
        else:
            args.extension = image.format
        print(args.size)
        print(args.aspectratio)
        print(args.extension)

