tls = 0
inpt = []

while True:
    l= input()
    if l=='':
        break
    inpt.append(l)

def findabba(str):
    for i in range(1,len(str) -1):
        if str[i:i+1] == str[i+1:i+2]:
            if str[i-1:i] == str[i+2:i+3]:
                if str[i:i+1] != str[i-1:i]:
                    return True
    return False

for l in inpt:
    support = True
    tmp = ''
    address = []
    hypernet = []
    for s in l:
        if (s == '['):
            address.append(tmp)
            tmp = ''
        elif (s == ']'):
            hypernet.append(tmp)
            tmp = ''
        else:
            tmp +=s
    if (tmp != ''):
        address.append(tmp)
    print(address, hypernet)
    for h in hypernet:
        if (findabba(h)):
            support = False
            break
    if support:
        for a in address:
            if (findabba(a)):
                tls +=1
                break

print(tls)


