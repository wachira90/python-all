#!python

import hashlib

x = b"1111"
hash = hashlib.md5(x)
print(hash.hexdigest()) 

hash = hashlib.sha1(b"1111") #ข้อความที่จะแฮชคือ 1111
print(hash.hexdigest())

hash = hashlib.sha224(b"1111") #ข้อความที่จะแฮชคือ 1111
print(hash.hexdigest())

hash = hashlib.sha256(b"1111") #ข้อความที่จะแฮชคือ 1111
print(hash.hexdigest())

hash = hashlib.sha384(b"1111") #ข้อความที่จะแฮชคือ 1111
print(hash.hexdigest())

#openSSL
hash = hashlib.new('ripemd160') 
hash.update(b"1111")  #ข้อความที่จะแฮชคือ 1111
print(hash.hexdigest())