import hashlib
import time

start = time.time()
password = [None] * 8
id = input()
n= 0

def printAnimation():
    anim = ''
    for n in password:
        if n is None:
            anim+='O'
        else:
            anim+='X'
    print(anim)

while True:
    test = id + str(n)
    test = test.encode('utf-8')
    m = hashlib.md5()
    m.update(test)
    hash = m.hexdigest()
    if hash.startswith('00000'):
        if hash[5:6].isdigit():
            pos = int (hash[5:6])
            if (pos<8 and password[pos] == None):
                password[pos] = hash[6:7]
                printAnimation()
                if (None not in password):
                    break
    n+=1
end = time.time()
print('Time elapsed:',end - start)
print('N:',n)
print('Pass:',"".join(password))
