import time

start = time.time()

inp = '^.....^.^^^^^.^..^^.^.......^^..^^^..^^^^..^.^^.^.^....^^...^^.^^.^...^^.^^^^..^^.....^.^...^.^.^^.^'
#inp = '.^^.^.^^^^'
ll = len(inp)

first = []
for l in inp:
    first.append(l == '^')

levels = [first]
safe = 0

def isTrap(x,y):
    if x == 0:
        if levels[y - 1][x + 1]:
            return True
    elif x == ll - 1:
        if levels[y - 1][x - 1]:
            return True
    else:
        if levels[y - 1][x - 1] != levels[y - 1][x + 1]:
            return True
    return False



for i in range(1,40):
    print(i)
    lvl = []
    for j in range(ll):
        lvl.append(isTrap(j,i))
    levels.append(lvl)

for level in levels:
    lvl = ''
    for l in level:
        if l:
            safe +=1
            lvl+='^'
        else:
            lvl+='.'
    print(lvl)
    #print(''.join(level))
    #safe +=level.count(True)
print('result:',safe)
print('Time elapsed:',(time.time() - start))