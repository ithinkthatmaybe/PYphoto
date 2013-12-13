from PIL import Image
import shutil
import os
import sys

##print "I am running, HAHAHAHA!"
##print "Arguments:", str(sys.argv)

global home = 'C:/users/sam/my photos/'
global target = 'C:/users/sam/my photos/'

def rip(rip_dir ,path = dir_current , filter_HDR = false):
    #Rip photos
    return


def HDR_filter(path = dir_current, time_window = 2, seperate = false,):
    
    return

def set_dir(path, type = 'home'):
    if type == 'home':
        home = path
    elif type == 'target':
        target = path
    else:
        print "type not recognised, path unchanged"

def dir_scan(path = home):
    print "Path = ", path
    


arg1 = str(sys.argv[1])
print "Arg: ", arg1

if arg1 == '-r':
    print "we are ripping from the camera"

elif arg1  == '-m':
    print "we are managing"
