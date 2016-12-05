import hashlib

password = ''

id = input()

n= 0
while True:
    test = id + str(n)
    test = test.encode('utf-8')
    m = hashlib.md5()
    m.update(test)
    hash = m.hexdigest()
    if hash.startswith('00000'):
        print(hash)
        password +=hash[5:6]
        if len(password)==8:
            break
    n+=1
print(password)
