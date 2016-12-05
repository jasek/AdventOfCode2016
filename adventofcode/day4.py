from collections import Counter

sum = 0

inpt = []


while True:
    l= input()
    if l=='':
        break
    inpt.append(l)
print(inpt)

for l in inpt:
    parts = l.split('-')
    last = parts.pop()
    lastlist = last.split('[')
    sector = int(lastlist[0])
    checksum = lastlist[1][:-1]
    print(parts,sector,checksum)
    j = "".join(parts)
    print(j)
    x = Counter(j)
    x =sorted(x.items(), key=lambda i: i[0])
    x = sorted(x, key=lambda i: i[1], reverse=True)
    check = ''
    for i in range(5):
        check+=x[i][0]
    print(check)
    if (check == checksum):
        sum+=sector
print(sum)
