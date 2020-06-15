import os
#TODO untested
def createoutputdir(path,dirname):
    fullpath = path + "/" + dirname
    accessrights = 0o755
    try:
        os.makedirs(fullpath,accessrights)
    except FileExistsError:
        fullpath = path + "/" + dirname
        try:
            os.makedirs(fullpath,accessrights)
        except FileExistsError:
            return False, "Folder already exists"
        except OSError as err:
            if(err.errno == errno.EEXIST):
                    return False, "FUCK"
    return True, None
