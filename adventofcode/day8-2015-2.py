import math

t1 = 0
t2 = 0

inpt = []


while True:
    l= input()
    if l=='':
        break
    inpt.append(l)

for l in inpt:
    tmp1 = len(l)
    t1+=tmp1
    n = l
    l = l.replace("\"","oo")
    l = l.replace("\\","oo")
    c = len(l)
    c += 2
    t2+=c
print(t1,t2,t2-t1)