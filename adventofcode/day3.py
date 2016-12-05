pos = 0

inpt = []


while True:
    l= input()
    if l=='':
        break
    inpt.append(l)
 

for l in inpt:
    list = []
    for s in l.strip().split(" "):
        m = s.strip()
        if (m != ''):
            list.append(int(m))
    list.sort()
    if (list[0]+list[1]>list[2]):
        pos +=1
       
print('Result:',pos)

