import subprocess
# subprocess.run(['python','devide.py'])

subprocess.run(['python','devide.py'],input='2',text=True)

'''
# 1 VARIABLE
# FILE devide.py
a = float(input())
print(a/11.)
'''


''' 
# 2 VARIABLE
subprocess.run(['python','sanpo.py'],input='2\n3',text=True)
'''

'''
# FILE sanpo.py
a = int(input())
b = int(input())
print('%d/%d = %s'%(a,b,a/b))
'''
