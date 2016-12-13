import os


sum = 0
inpt = []
dspl = []

for i in range(6):
    dspl.append(' ' * 50)

def printRect():
    os.system('cls')
    for l in dspl:
       row = ''.join(l)
       row = row.replace('#', '\u2588')
       row = row.replace(' ', '\u2592')
       print(row)

while True:
    l= input()
    if l=='':
        break
    inpt.append(l)

for l in inpt:
    if l.startswith('rect'):
        size = l[5:]
        a,b = [int(x) for x in size.split('x')]
        for i in range(b):
            for j in range(a):
                dspl[i] = dspl[i][:j] +  '#' + dspl[i][j+1:]
    elif l.startswith('rotate row'):
        size = l[13:]
        a,b = [int(x) for x in size.split(' by ')]
        dspl[a] = dspl[a][50-b:] +  dspl[a][:50-b]
    elif l.startswith('rotate column'):        
        size = l[16:]
        a,b = [int(x) for x in size.split(' by ')]
        col = ''
        for i in range(6):
            col += dspl[i][a]
        col = col[6-b:] + col[:6-b]
        for i in range(6):
            dspl[i] = dspl[i][:a] + col[i] + dspl[i][a+1:]
    printRect()
for l in dspl:
    sum += l.count('#')
print('sum:',sum)
        






