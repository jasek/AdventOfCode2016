m = [[1,2,3],[4,5,6],[7,8,9]]
x=1
y=1

inpt = []
res = ''

while True:
    l= input()
    if l=='fin':
        break
    inpt.append(l)
print(inpt)   

for l in inpt:
    for s in l:
        if (s == 'U' and y>0):
            y-=1
        elif (s == 'D' and y<2):
            y+=1
        elif (s == 'L' and x >0):
            x -=1
        elif (s == 'R' and x <2):
            x +=1
    res += str(m[y][x])
print(res)