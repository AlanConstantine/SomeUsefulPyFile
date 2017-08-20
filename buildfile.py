import os
import shutil


def buildfile(echkeyfile):
    if os.path.exists(echkeyfile):
        shutil.rmtree(echkeyfile)
        os.makedirs(echkeyfile)
    else:
        os.makedirs(echkeyfile)
    return echkeyfile
