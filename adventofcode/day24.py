import time
import itertools

start = time.time()
lines = open('input24.txt', 'r').read().splitlines()

numbers = ('0','1','2','3','4','5','6','7',)
PIXON = '\u2588'
PIXOFF = '\u2592'
PIXV = '.'
PIXW = 'x'
parents = dict()
pos = dict()
maze = []
queue = []
visited = []
tovisit = [1,2,3,4,5,6,7]
#[7,1,3,6,5,4,2] 514
#[7,1,3,6,4,5,2] 490
def printMaze(m):
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
            if s == '.':
                ln += PIXOFF
            elif s == '#':
                ln += PIXON
            elif s == 'o':
                ln += '.'
            else:
                ln +=s
        print(str(l).zfill(2) + ' ' + ln)



for l in lines:
    maze.append(list(l))
    #print(list(l))

#print(maze)
for l in range(len(maze)):
    for t in range(len(maze[l])):
        if maze[l][t] in numbers:
            pos[int(maze[l][t])] = (t,l)

def getChildren(node):
    child = []
    x = node[0]
    y = node[1]
    if x - 1 >= 0:
        if maze[y][x - 1] != '#' and maze[y][x - 1] != 'v':
            child.append((x - 1,y))
    if y + 1 < len(maze):
        if maze[y + 1][x] != '#' and maze[y + 1][x] != 'v':
            child.append((x,y + 1))
    if x + 1 < len(maze[0]):
        if maze[y][x + 1] != '#' and maze[y][x + 1] != 'v':
            child.append((x + 1,y))
    if y - 1 >= 0:
        if maze[y - 1][x] != '#' and maze[y - 1][x] != 'v':
            child.append((x,y - 1))
    return child



def addParents(parent, children):
    for child in children:
        parents[child] = parent



def bfs(startNode, endNode):
    queue = []
    queue.append(startNode)
    while len(queue) > 0:
        node = queue.pop(0)
        #visited.add(node)
        maze[node[1]][node[0]] = 'v'
        printMaze(maze)
        if node == endNode:
            return
        else:
            children = getChildren(node,maze)
            addParents(node, children)
            queue.extend(children)

def heuristic_cost_estimate(start, goal):
    return abs(goal[0] - start[0]) + abs(goal[1] - start[1])

def getLowestValue(openSet, fScore):
    min = 1000000
    lowest = None
    for n in openSet:
        if fScore[n] < min:
            min = fScore[n]
            lowest = n
    return lowest

def findWay(parents, node):
    way = []
    c = node
    while c in parents:
        way.append(c)
        c = parents[c]
    return way


def astar(start, goal):
    closedSet = set()
    openSet = {start}
    cameFrom = dict()
    gScore = dict()
    gScore[start] = 0
    fScore = dict()
    fScore[start] = heuristic_cost_estimate(start, goal)

    while len(openSet) > 0:
        current = getLowestValue(openSet, fScore)
        #maze[current[1]][current[0]] = 'l'
        #printMaze(maze)
        if current == goal:
            return findWay(cameFrom, current)
        openSet.remove(current)
        closedSet.add(current)
        for neighbor in getChildren(current):
            if neighbor in closedSet:
                continue
            tentative_gScore = gScore[current] + 1
            if neighbor not in openSet:
                openSet.add(neighbor)
            elif tentative_gScore >= gScore[neighbor]:
                continue

            cameFrom[neighbor] = current
            gScore[neighbor] = tentative_gScore
            fScore[neighbor] = gScore[neighbor] + heuristic_cost_estimate(neighbor, goal)

    return 'lol'


printMaze(maze)



def markWay(way):
    for n in way:
        if maze[n[1]][n[0]] == '.':
            maze[n[1]][n[0]] = 'o'




#for p in itertools.permutations(tovisit):
#    print(p)


total = 10000
for j in itertools.permutations(tovisit):
    j = list(j)
    j.append(0)
    print(j)
    solution = []
    current = 0    
    shortest = 1000
    sol = None
    shortway = None
    for i in j:
        visited = set()
        parents = dict()
        way = astar(pos[current], pos[i])
        print(len(way))
        shortest = len(way)
        sol = (current, i)
        shortway = way
        #markWay(way)
        #printMaze(maze)
        solution.append((shortest,sol, shortway))
        #tovisit.remove(sol[1])
        current = sol[1]

    totalWay = 0
    for sol in solution:
        totalWay += sol[0]
    if totalWay < total:
        total = totalWay
    print('totalway',totalWay)
    print('total',total)
print('total',total)

printMaze(maze)

print('Time elapsed:',time.time() - start)


# [(30, (0, 1)), (30, (1, 3)), (66, (3, 6)), (126, (6, 7))]