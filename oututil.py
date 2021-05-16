import os
import errorwindow

def createoutputdir(path,dirname):
    if(not path or path == "" or  not dirname):
       return False, "No output folder defined!", None
    print(path, "+",dirname)
    fullpath = path + "/" + dirname
    accessrights = 0o755
    try:
        os.makedirs(fullpath,accessrights)
    except FileExistsError:
        return False,"FileExistsError: Output folder already exists.",None
    except OSError as err:
            if(err.errno == errno.EEXIST):
                return False, "OSError: Could not create outputfolder.",None
    except PermissionError:
        return False,"PermissionError: Could not create output folder.",None
    return True, None, fullpath
