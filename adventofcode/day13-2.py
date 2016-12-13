fn = 1364
m = []
solution = (31,39)
start = (1,1)
size = 50
mmvs = 50

PIXON = '\u2588'
PIXOFF = '\u2592'
PIXV = '.'
PIXW = 'x'
parents = dict()
def calculate(x, y):
    return x * x + 3 * x + 2 * x * y + y + y * y + fn

def evenBinaryZeros(i):
    return 0 if bin(i)[2:].count('1') % 2 == 0 else 1


def createMatrix(size):
    for i in range(size):
        row = []
        for j in range(size):
            row.append(evenBinaryZeros((calculate(j,i))))
        m.append(row)

def printMatrix():
    fr = '   '
    fr2 = '   '
    for i in range(len(m)):
        fr += str(i)[-1:]
        fr2 += str(i).zfill(2)[:1]
    print(fr2)
    print(fr)
    for l in range(len(m)):
        ln = ''
        for s in m[l]:
            if s == 0:
                ln += PIXOFF
            elif s ==1:
                ln += PIXON
            elif s ==2:
                ln += PIXV
            elif s ==3:
                ln += PIXW
        print(str(l).zfill(2) + ' ' + ln)

def export():
    for l in m:
        print(';'.join(l))

def getChildren(node):
    child = []
    x = node[0]
    y = node[1]
    if x - 1 >= 0:
        if m[y][x - 1] == 0:
            child.append((x - 1,y))
    if y+1<size:
        if m[y+1][x] == 0:
            child.append((x,y+1))
    if x+1<size:
        if m[y][x+1] == 0:
            child.append((x+1,y))
    if y - 1 >= 0:
        if m[y-1][x] == 0:
            child.append((x,y-1))
    return child

def markVisited(node):
    m[node[1]][node[0]] = 2

def addParents(parent, children):
    for child in children:
        parents[child] = parent

def solve(startNode):
    queue = []
    queue.append(startNode)
    while len(queue) > 0:
        node = queue.pop(0)
        markVisited(node)
        children = getChildren(node)
        addParents(node, children)
        queue.extend(children)

def findWay(node):
    way = []
    c = node
    while c != start:
        way.append(c)
        c = parents[c]
    return way

def markWay(way):
    for node in way:
        m[node[1]][node[0]] = 3


def findVisitedForMax(mmvs):
    res = []
    for p in parents:
        way = findWay(p)
        if len(way)<=mmvs:
            res.append(p)
    return res

createMatrix(size)

printMatrix()

print(calculate(0,2))
print(bin(calculate(0,2)))
print(evenBinaryZeros(calculate(1,1)))

print(getChildren((9,1)))
solve(start)
printMatrix()

#way = findWay(solution)
#markWay(way)
printMatrix()
#print(len(way), way)

vis = findVisitedForMax(mmvs)
print(vis,len(vis)+1)