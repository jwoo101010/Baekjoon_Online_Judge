import base64,zlib,hashlib

def nne(s):return base64.b16encode(zlib.compress(s.encode('UTF-8'))).decode()
a=''
while 1:
    try:
        a+=input()+'\n'
    except:break
s=hashlib.sha1(nne(a).encode()).hexdigest().upper()
q=s+nne(a)+s
print(q)
print(len(q),len(a),len(nne(a)))
