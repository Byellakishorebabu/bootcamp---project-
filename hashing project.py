import hashlib
strhash='dilip'
result=hashlib.md5(strhash.encode())
print('the md5 hash encrypt is:',end='')
print(result.hexdigest())
