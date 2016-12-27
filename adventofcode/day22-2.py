 

lines = open('input22.txt', 'r').read().splitlines()

pairs = []
nodes = []

matrix = []

bigx = 0
bigy = 0


class Node:
    def __init__(self, name, size, used, avail, use):
        self.name = name
        self.size = size
        self.used = used
        self.avail = avail
        self.use = use
    def __str__(self):
        if self.use > 90:
            return '#'
        elif self.used == 0:
            return '_'
        else:
            return '.'


def printMatrix():
    firstline = '    '
    secondline = '    '
    for x in range(bigx+1):
        numb = str(x).zfill(2)
        firstline += numb[:1]
        secondline += numb[1:]
    print(firstline)
    print(secondline)
    for y in range(bigy+1):
        line = str(y).zfill(2) + ': '
        for x in range(bigx+1):
            line += ';'+str(matrix[x][y])
        print(line)

def isViableInOrder(node1, node2):
    return node1[2] > 0 and node1[2] <= node2[3]

def isPairViable(node1, node2):
    if isViableInOrder(node1, node2):
        return True
    elif isViableInOrder(node2, node1):
        return True
    else:
        return False

lastx = 0
col = []
for l in range(2,len(lines)):
    node = lines[l].split()
    nodeo = Node(node[0],int(node[1][:-1]),int(node[2][:-1]),int(node[3][:-1]),int(node[4][:-1]))
    pos = node[0].split('-')
    x = int(pos[1][1:])
    y = int(pos[2][1:])
    if x > bigx:
        bigx = x
    if y > bigy:
        bigy = y
    if lastx != x:
        lastx = x
        matrix.append(col)
        col = []
    col.append(nodeo)
    print(x,y,node)
matrix.append(col)
'''for i in range(len(nodes)):
    for j in range(i + 1, len(nodes)):
        #print(nodes[i],nodes[j])
        if isPairViable(nodes[i],nodes[j]):
            pairs.append((nodes[i],nodes[j]))'''

print(len(matrix),len(matrix[0]))
printMatrix()