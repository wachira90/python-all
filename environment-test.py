#!python3
import os

for item, value in os.environ.items():
    print('{}: {}'.format(item, value))

'''
for i, j in os.environ.items():
    print(i, j)
    

print(os.environ['HOME'])

print(os.environ.get('HOME'))

os.environ['HOME'] = '/new/value'

'''
