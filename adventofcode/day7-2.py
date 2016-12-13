import time

ssl = 0
inpt = []

while True:
    l= input()
    if l=='':
        break
    inpt.append(l)

def findabas(str):
    abas = []
    for i in range(len(str) -2):
        if str[i:i+1] == str[i+2:i+3]:
                if str[i:i+1] != str[i+1:i+2]:
                    abas.append(str[i:i+3])
    return abas
start = time.time()
for l in inpt:
    support = False
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
    #print(address, hypernet)
    abas = []
    for a in address:
        abas.extend(findabas(a))
    #print('abas',abas)
    for aba in abas:
        bab = aba[1:2]+aba[0:1]+aba[1:2]
        for h in hypernet:
            if bab in h:
                #print('bab',bab)
                #print('ssl',ssl)
                support = True
                break
        if support:
            break
    if support:
        ssl +=1

print('ssl',ssl)


end = time.time()
print('Time elapsed:',end - start)