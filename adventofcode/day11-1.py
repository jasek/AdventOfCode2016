import sys
import time

start = time.time()
solutions = []
iterations = 0
queue = []
visited = set()
elements = []

def isFloorCorrect(floor):
    for el in floor:
        if el[1:2] == 'M':
            if el[0:1] + 'G' not in floor:
                for gen in floor:
                    if gen[1:2] == 'G':
                        return False
    return True

def getDoubleCombos(floor):
    floor = list(floor)
    res = []
    lenght = len(floor)
    pair = False
    for i in range(lenght - 1):
        for j in range(i + 1, lenght):
            if  floor[i][:1] == floor[j][:1]:
                if not pair:
                    res.append([floor[i],floor[j]])
                    pair = True
            else:                
                res.append([floor[i],floor[j]])
    return res

def getUpCombos(floor):
    pairg = False
    pairm = False
    if len(floor) == 0:
        return []
    if len(floor) == 1:
        return [floor]
    if len(floor) == 2:
        pos = []
        pos.append(floor)
        for x in floor:
            pos.append([x])
        return pos
    if len(floor) > 2:
        pos = []
        pos.extend(getDoubleCombos(floor))
        for x in floor:
            if x[1:] == 'M':
                if x[:1]+'G' in floor:
                    if not pairm:
                        pos.append([x])
                        pairm = True
                else:
                    pos.append([x])
            else:
                if x[:1]+'M' in floor:
                    if not pairg:
                        pos.append([x])
                        pairg = True
                else:
                    pos.append([x])
        return pos

def getDownCombos(floor):
    pairg = False
    pairm = False
    if len(floor) == 0:
        return []
    pos = []
    for x in floor:
        pos.append([x])
    return pos

def addToQueue(sol):
    tup = sol.arrangment.pairs
    if tup in visited:
        return
    visited.add(tup)
    queue.append(sol)

def getElements(floors):
    elements = []
    for fl in floors:
        for el in fl:
            if el[:1] not in elements:
                elements.append(el[:1])
    elements.sort()
    return elements


class Arrangment:
    global elements
    def __init__(self, floors, elevator):
        self.elevator = elevator
        self.floors = floors
        self.pairs = self.getPairs()
    def equals(self, arr):
        return self.floors == arr.floors and self.elevator == arr.elevator
    def print(self):
        for l in range(len(self.floors)):
            print(4-l,' ', 'E   ' if self.elevator == 3-l else '    ','   ',self.floors[3-l])
    def isCorrect(self):
        for f in self.floors:
            if not isFloorCorrect(f):
                return False
        return True
    def isFinished(self):
        if len(self.floors[0]) == 0 and len(self.floors[1]) == 0 and len(self.floors[2]) == 0:
            return True
        return False
    def getPairs(self):
        pairs = []
        for el in elements:
            g = -1
            m = -1
            for floorn in range(len(self.floors)):
                if el+'G' in self.floors[floorn]:
                    g = floorn
                if el+'M' in self.floors[floorn]:
                    m = floorn
            pairs.append((g,m))
        pairs.sort()
        pairs.append(self.elevator)
        return tuple(pairs)

class Solution:
    def __init__(self, arrangment, parent, step):
        self.arrangment = arrangment
        self.parent = parent
        self.step = step
    def print(self):
        self.arrangment.print()
        print('step',self.step)
    def printToRoot(self):
        if self.parent != None:
            self.print()
            self.parent.printToRoot()

def solve():
    global iterations
    while True:
        cur = queue.pop(0)
        iterations +=1
        if (cur.arrangment.isFinished()):
            cur.printToRoot()
            print('res',cur.step)
            return
        if cur.arrangment.elevator < 3:
            for el in getUpCombos(cur.arrangment.floors[cur.arrangment.elevator]):
                sol =  moveUp(cur, el)
                if sol.arrangment.isCorrect():
                    addToQueue(sol)
        if cur.arrangment.elevator > 0:
            for el in getDownCombos(cur.arrangment.floors[cur.arrangment.elevator]):
                sol =  moveDown(cur, el)
                if sol.arrangment.isCorrect(): 
                    addToQueue(sol)

def moveUp(sol, combo):
    newFloors = []
    for i in range(len(sol.arrangment.floors)):
        fl = set()
        if i == sol.arrangment.elevator:
            for el in sol.arrangment.floors[i]:
                if el not in combo:
                    fl.add(el)
        elif i == sol.arrangment.elevator +1:
            fl.update(sol.arrangment.floors[i])
            fl.update(combo)
        else:
            fl.update(sol.arrangment.floors[i])
        newFloors.append(fl)
    return Solution(Arrangment(newFloors, sol.arrangment.elevator + 1), sol, sol.step + 1)

def moveDown(sol, combo):
    newFloors = []
    for i in range(len(sol.arrangment.floors)):
        fl = set()
        if i == sol.arrangment.elevator:
            for el in sol.arrangment.floors[i]:
                if el not in combo:
                    fl.add(el)
        elif i == sol.arrangment.elevator - 1:
            fl.update(sol.arrangment.floors[i])
            fl.update(combo)
        else:
            fl.update(sol.arrangment.floors[i])
        newFloors.append(fl)
    return Solution(Arrangment(newFloors, sol.arrangment.elevator - 1), sol, sol.step + 1)

   
part1 = [{'TG','TM','PG','SG'},{'PM','SM'},{'HG','HM','RG','RM'},set()]
part2 = [{'EG','EM','DG','DM','TG','TM','PG','SG'},{'PM','SM'},{'HG','HM','RG','RM'},set()]

initSolution = Solution(Arrangment(part1, 0), None, 0)
addToQueue(initSolution)
elements = getElements(part1)
solve()
queue = []
#initSolution2 = Solution(Arrangment(part2, 0), None, 0)
#addToQueue(initSolution2)
#elements = getElements(part2)
#solve()
print('iterations',iterations)
print('Time elapsed:',time.time() - start)