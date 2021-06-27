#!python
import sys
  
add = 0.0
  
# Getting the length of command
# line arguments
n = len(sys.argv)
  
for i in range(1, n):
    add += float(sys.argv[i])
  
print ("the sum is :", add)

'''
python test-argv1.py 3.14 2.89 4.44
the sum is : 10.47
'''
