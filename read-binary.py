#!D:\python37\python.exe
#-*- coding: utf-8 -*-

import io

# f = open("testfile.txt", "rb", buffering=0)
# print(f)

b = io.BytesIO(b"abcdef")
view = b.getbuffer()
print(view)
view[2:4] = b"56"
x= b.getvalue()
print(x)
