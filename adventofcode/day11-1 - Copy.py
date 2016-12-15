import sys
import time
#sys.setrecursionlimit(10000)
solutions = []

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
    for i in range(lenght - 1):
        for j in range(i + 1, lenght):
            res.append([floor[i],floor[j]])
    return res


def getUpCombos(floor):
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
            pos.append([x])
        return pos

def getDownCombos(floor):
    if len(floor) == 0:
        return []
    pos = []
    for x in floor:
        pos.append([x])
    return pos


mins = set()
min = 40


queue = []
visited = []

def addToQueue(sol):
    for v in visited:
        if v.equals(sol.arrangment):
            return
    visited.append(sol.arrangment)
    queue.append(sol)


class Arrangment:
    def __init__(self, floors, elevator):
        self.elevator = elevator
        self.floors = floors
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
            self.parent.print()

def solve():
    while True:
        cur = queue.pop(0)
        cur.print()
        print(len(queue))
        if (cur.arrangment.isFinished()):
            print('fuck yeah')
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

    
#initFloors = [{'TG','TM','PG','SG'},{'PM','SM'},{'HG','HM','RG','RM'},set()]
initFloors = [{'EG','EM','DG','DM','TG','TM','PG','SG'},{'PM','SM'},{'HG','HM','RG','RM'},set()]


a1 = Arrangment(initFloors, 0)
initSolution = Solution(a1, None, 0)
addToQueue(initSolution)
solve()


