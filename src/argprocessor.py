import processwindow as pw
from collections import deque
from PIL import Image


#arg-object to pass on to imageresizing module
class Resize_options:
    def __init__ (self,aspectratio=0,target_size=(),ogsize=(),extension=None,imgpath=None,outputpath=None,multithreading=False, jpegquality=90):
        self.aspectratio= aspectratio
        self.target_size= target_size 
        self.extension  = extension
        self.outputpath = outputpath
        self.ogsize     = ogsize
        self.imgpath    = imgpath
        self.jpegquality= jpegquality

def process(root,filepath,imgpaths,outputpath,gui_args):
    #print(f"MH:{gui_args["maxheight"]} MW:{gui_args["maxwidth"]}")
    print(gui_args)
    master = root
    resize_options = deque()
    image_height = image_width = 0.0
    val_aspectratio = 0.0

    #parse gui arguments in to arg object
    for i in range(len(imgpaths)):
        resize_opt = Resize_options()
        image = Image.open(imgpaths[i])
        image_width, image_height = image.size
        resize_opt.imgpath         = imgpaths[i]
        resize_opt.jpegquality = gui_args.get("jpegquality",80)
        target_height       = target_width = 0
        resize_opt.extension       = (gui_args["userextension"],image.format)[gui_args["preserveextensions"]]
        resize_opt.outputpath      = outputpath
        target_height       = get_targetsize(gui_args["maxheight"],image_height)
        target_width        = get_targetsize(gui_args["maxwidth"],image_width)
        resize_opt.aspectratio     = (target_width/target_height,image_width/image_height)[gui_args["aspectratio"]]
        resize_opt.multithreading  = (False,True)[gui_args["multithreading"]]
        
        #is max height/width defined in GUI?
        if(gui_args["maxheight"] > 0):
            maxheight = (gui_args["maxheight"],target_height)[gui_args["maxheight"]==target_height]
        else:
            maxheight = 0
        if(gui_args["maxwidth"] > 0):
            maxwidth = (gui_args["maxwidth"],target_width)[gui_args["maxwidth"]==target_width]
        else:
            maxwidth = 0
        
        #is aspectratio defined in GUI
        if(gui_args["aspectratio"]):
            #is height larger than defined max height when image is resized by max width
            #if true, then resize height first, then width, so target_height <= maxheigt and vice versa
            if(maxheight > 0 and maxwidth > 0):
                tempwidth = target_height * resize_opt.aspectratio
                tempheight = tempwidth / resize_opt.aspectratio
                if(tempwidth > target_width):
                    target_height = target_width / resize_opt.aspectratio
                    target_width = target_height * resize_opt.aspectratio
                else:
                    target_width = target_height * resize_opt.aspectratio
                    target_height = target_width / resize_opt.aspectratio
            elif(maxheight > 0 and maxwidth <= 0):
                target_width = target_height * resize_opt.aspectratio
            elif(maxheight <= 0 and maxwidth > 0):
                target_height = target_width / resize_opt.aspectratio
            else:
                print(f"Can not calculate aspect ratio: maxheight:{maxheight} maxwidth:{maxwidth} target_height:{ target_height} target_width:{target_width}")
        target_width = int(target_width)
        target_height= int(target_height)
        resize_opt.target_size = target_width,target_height
        resize_options.append(resize_opt)

    process = pw.ProcessWindow(master,resize_options,gui_args["multithreading"],False)

def get_targetsize(xy_target,xy_image):
    target = 0;
    if(xy_target > 0 and xy_target<=xy_image):
        target = xy_target
    elif(xy_target > 0 and xy_target>xy_image):
        target = xy_image
    else:
        target = xy_image
    return target

