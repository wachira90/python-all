#!python
# -*- coding: utf-8 -*-

import xlrd 
import os

loc = ("file1.xlsx") 

wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 

# For row 0 and column 0 
sheet.cell_value(0, 0) 

# print("|",end = '')
# for c in range(sheet.ncols):
# 	print(sheet.cell_value(0, c), end = '|') 

# for c in range(sheet.ncols):
# 	print(sheet.cell_value(0, c)) 

# for i in range(sheet.nrows):
#         print(sheet.cell_value(i, 0))

for r in range(sheet.nrows):
    print ("",end = '')
    for c in range(sheet.ncols):
        if (sheet.ncols == 13):
            print (sheet.cell_value(r, c).strip(), end = '')
        else: 
            print (sheet.cell_value(r, c).strip(), end = ',') 
        # print(sheet.cell_value(i, 0))
    print ("")
# print("SUCCESS...",sheet.nrows)