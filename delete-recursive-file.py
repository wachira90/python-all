#!python
import os
import glob

# Get a list of all the file paths that ends with .txt from in specified directory
fileList = glob.glob('/home/varung/Documents/python/logs/*.log')

# Iterate over the list of filepaths & remove each file.
for filePath in fileList:
    try:
        os.remove(filePath)
    except:
        print("Error while deleting file : ", filePath)

'''
# Get list of files using glob.glob()
glob.glob(pathname, *, recursive=False)
'''
