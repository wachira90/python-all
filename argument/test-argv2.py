#!python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--name", required=True)
args = parser.parse_args()
print(f'Hi {args.name} , Welcome ')

'''
(venv) C:\Users\Nandank\PycharmProjects\DSA\venv>python argparse_ex.py --name Nandan 
Hi Nandan , Welcome 
(venv) C:\Users\Nandank\PycharmProjects\DSA\venv>python argparse_ex.py -n Nandan 
Hi Nandan , Welcome 
'''
