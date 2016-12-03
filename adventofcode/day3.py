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
    if (i>2):
        i = 0

    list = []
    for s in l.strip().split(" "):
        m = s.strip()
        if (m != ''):
            list.append(int(m))
    list.sort()
    if (list[0]+list[1]>list[2]):
        print('possible')
        pos+=1
print(pos)

