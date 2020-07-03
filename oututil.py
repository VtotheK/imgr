import os
#TODO untested

def createoutputdir(path,dirname):
    fullpath = path + "/" + dirname
    accessrights = 0o755
    try:
        os.makedirs(fullpath,accessrights)
    except FileExistsError:
        return False,"FileExistsError: Output folder already exists."
    except OSError as err:
            if(err.errno == errno.EEXIST):
                return False, "OSError: Could not create outputfolder." 
    except PermissionError:
        return False,"PermissionError: Could not create output folder."
    return True, None
