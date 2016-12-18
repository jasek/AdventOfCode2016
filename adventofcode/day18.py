inp = '^.....^.^^^^^.^..^^.^.......^^..^^^..^^^^..^.^^.^.^....^^...^^.^^.^...^^.^^^^..^^.....^.^...^.^.^^.^'
#inp = '.^^.^.^^^^'
ll = len(inp)

levels = [list(inp)]
safe = 0

def isTrap(x,y):
    if x == 0:
        if levels[y - 1][x + 1] == '^':
            return True
    elif x == ll - 1:
        if levels[y - 1][x - 1] == '^':
            return True
    else:
        if levels[y - 1][x - 1] == '^' and levels[y - 1][x + 1] == '.':
            return True
        if levels[y - 1][x + 1] == '^' and levels[y - 1][x - 1] == '.':
            return True
    return False



for i in range(1,400000):
    print(i)
    lvl = []
    for j in range(ll):
        lvl.append('^' if isTrap(j,i) else '.')
    levels.append(lvl)

for level in levels:
    print(''.join(level))
    safe +=level.count('.')
print('result:',safe)