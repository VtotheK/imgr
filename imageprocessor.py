from PIL import Image


def process(filepath,imgpaths,maxheight=None,maxwidth=None,perserveextensions=True,userextension=None,aspectratio=True):
    target_height = target_width = 0
    image_height = image=width = 0
    aspectratio = 0.0
    for i in range(len(imgpaths)):
        image = Image.open(imgpaths[i])
        if(aspectratio):
            image_width, image_height = image.size
            aspectratio = image_width / image_height
            print(aspectratio)
