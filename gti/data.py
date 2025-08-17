""" this file deals with the .gti repository """

import os

# REMEMBER: gti dir, not git dir like the tutorial
GTI_DIR = '.gti'

def init():
    os.makedirs(GTI_DIR)