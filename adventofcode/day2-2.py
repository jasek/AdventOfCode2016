m = [['.','.','1','.','.'],['.','2','3','4','.'],['5','6','7','8','9'],['.','A','B','C','.'],['.','.','D','.','.']]
x=0
y=2

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
        if (s == 'U' and y>0 and m[y-1][x]!='.'):
            y-=1
        elif (s == 'D' and y<4 and m[y+1][x]!='.'):
            y+=1
        elif (s == 'L' and x >0 and m[y][x-1]!='.'):
            x -=1
        elif (s == 'R' and x <4 and m[y][x+1]!='.'):
            x +=1
    res += str(m[y][x])
print(res)