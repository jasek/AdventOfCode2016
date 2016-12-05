pos = 0

inpt = []


while True:
    l= input()
    if l=='fin':
        break
    inpt.append(l)
print(inpt)   
i =0
t1 =[]
t2=[]
t3=[]
for l in inpt:
    i +=1

    list = []
    for s in l.strip().split(" "):
        m = s.strip()
        if (m != ''):
            list.append(int(m))
    t1.append(list[0])
    t2.append(list[1])
    t3.append(list[2])
    if (i>2):
        i = 0
        print(t1,t2,t3)
        t1.sort()
        t2.sort()
        t3.sort()
        if (t1[0]+t1[1]>t1[2]):
            print('t1possible')
            pos+=1
        if (t2[0]+t2[1]>t2[2]):
            print('t2possible')
            pos+=1
        if (t3[0]+t3[1]>t3[2]):
            print('t3possible')
            pos+=1
        t1 =[]
        t2=[]
        t3=[]


print(pos)

