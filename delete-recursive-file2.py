#!python
import os
import glob

# get a recursive list of file paths that matches pattern including sub directories
fileList = glob.glob('/home/varung/Documents/python/logs/**/*.txt', recursive=True)

# Iterate over the list of filepaths & remove each file.
for filePath in fileList:
    try:
        os.remove(filePath)
    except OSError:
        print("Error while deleting file")
