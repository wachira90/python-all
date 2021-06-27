#!python

import os , sys 

dirName = './chkdir-exist'

try:
    os.mkdir(dirName)
    print("Directory " , dirName ,  " Created ") 
except FileExistsError:
# except :
    print("Directory " , dirName ,  " already exists")    