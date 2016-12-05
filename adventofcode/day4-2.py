from collections import Counter

sum = 0

inpt = []


while True:
    l= input()
    if l=='':
        break
    inpt.append(l)
northsector = 0

for l in inpt:
    parts = l.split('-')
    lastlist = parts.pop().split('[')
    sector = int(lastlist[0])
    checksum = lastlist[1][:-1]
    j = " ".join(parts)
    j = list(j)
    mv = sector%26
    for i in range(len(j)):
        if j[i] != ' ':
            l = j[i]
            num = ord(l)
            num += mv
            if num > ord('z'):
                num -= 26
            elif num < ord('a'):
                num += 26
            j[i] = chr(num)
    if 'north' in ''.join(j):
        northsector = sector
print('North sector object sotrage:', northsector)

