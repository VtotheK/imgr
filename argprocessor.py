from PIL import Image
import processwindow as pw

class Resize_options:
    def __init__ (self,aspectratio=0,target_size=(),ogsize=(),extension=None,outputpath=None,multithreading=False):
        self.aspectratio= aspectratio
        self.target_size= target_size 
        self.extension  = extension
        self.outputpath = outputpath
        self.ogsize     = ogsize
        self.multithreading = multithreading 

def process(root,filepath,imgpaths,outputpath,maxheight,maxwidth,preserveextensions=True,userextension=None,aspectratio=True,multithreading=False):
    print(f"MH:{maxheight} MW:{maxwidth}")
    master = root
    arg = Resize_options()
    args = []
    args.multithreading = multithreading
    image_height = image_width = 0.0
    val_aspectratio = 0.0
    for i in range(len(imgpaths)):
        image = Image.open(imgpaths[i])
        image_width, image_height = image.size
        target_height       = target_width = 0
        arg.extension      = (userextension,image.format)[preserveextensions]
        target_height       = get_targetsize(maxheight,image_height)
        target_width        = get_targetsize(maxwidth,image_width)
        arg.aspectratio = (target_width/target_height,image_width/image_height)[aspectratio]
        if(maxheight > 0):
            maxheight = (maxheight,target_height)[maxheight==target_height]
        if(maxwidth > 0):
            maxwidth = (maxwidth,target_width)[maxwidth==target_width]
        if(aspectratio):
            if(maxheight > 0 and maxwidth > 0):
                tempwidth = target_height * arg.aspectratio
                tempheight = tempwidth / arg.aspectratio
                if(tempwidth > target_width):
                    target_height = target_width / args.aspectratio
                    target_width = target_height * args.aspectratio
                else:
                    target_width = target_height * args.aspectratio
                    target_height = target_width / args.aspectratio
            elif(maxheight > 0 and maxwidth <= 0):
                target_width = target_height * args.aspectratio
            elif(maxheight <= 0 and maxwidth > 0):
                target_height = target_width / args.aspectratio
            else:
                print(f"Can not calculate aspect ratio: maxheight:{maxheight} maxwidth:{maxwidth} target_height:{ target_height} target_width:{target_width}")
        arg.target_size = target_width,target_height
        args.append(arg)
        """
        print(f"imagepath{imgpaths[i]}")
        print(f"originalsize{image.size}")
        print(f"targetsize :{args.target_size}")
        print(f"aspectratio:{args.aspectratio}")
        print(f"extension:{args.extension}\n")
        """
    process = pw.ProcessWindow(root=master,None,None,None,False)
#LEVEYS = KORKEUS * ASPECTRATIO
def get_targetsize(xy_target,xy_image):
    target = 0;
    if(xy_target > 0 and xy_target<=xy_image):
        target = xy_target
    elif(xy_target > 0 and xy_target>xy_image):
        target = xy_image
    else:
        target = xy_image#TODO THIS SECTION STINKS
    return target

