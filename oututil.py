import os


def createoutputdir(path,dirname):
    fullpath = path + "/" + dirname
    accessrights = 0o777
    tries = 0
    index = -1
    created = False
    try:
        os.makedirs(fullpath,accessrights)
    except FileExistsError:
        while(not created or tries < 100):
            index = index + 1
            fullpath = path + "/" + dirname + str(index)
            tries = tries + 1
            try:
                os.makedirs(fullpath,accessrights)
                created = True
            except FileExistsError:
                pass
            except OSError as err:
                if(err.errno == errno.EEXIST):
                        return false
    return True
