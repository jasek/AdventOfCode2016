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

class Solution:
    def __init__(self, elevator, floors, parent, step, lastDir, lastComb):
        self.elevator = elevator
        self.floors = floors
        self.parent = parent
        self.step = step
        self.lastDir = lastDir
        self.lastComb = lastComb
    def print(self):
        print('#######################')
        for l in range(len(self.floors)):
            print(4-l,' ', 'E   ' if self.elevator == 3-l else '    ','   ',self.floors[3-l])
    def solve(self):
        global min
        #if self.step % 10 == 0:
        self.print()
        print(self.step)
        #time.sleep(0.1)
        if self.elevator < 3:
            for el in getUpCombos(self.floors[self.elevator]):
                #do something
                #print('up', el)
                if self.lastDir == 'u' or el != self.lastComb:
                    sol =  self.moveUp(el)
                    if sol.step < min and sol.isCorrect():
                        if sol.isFinished():
                            mins.add(sol.step)
                            min = min(mins)
                            print('######### fin',sol.step, min)
                            break
                        else:
                            sol.solve()
        if self.elevator > 0:
            for el in getDownCombos(self.floors[self.elevator]):
                if self.lastDir == 'd' or el != self.lastComb:
                    #do something
                    #print('down', el)
                    sol =  self.moveDown(el)
                    if sol.step < min and sol.isCorrect():
                        sol.solve()
    def isCorrect(self):
        for f in self.floors:
            if not isFloorCorrect(f):
                return False
        return True
    def isFinished(self):
        if len(self.floors[0]) == 0 and len(self.floors[1]) == 0 and len(self.floors[2]) == 0:
            return True
        return False
    def moveUp(self, combo):
        newFloors = []
        for i in range(len(self.floors)):
            fl = []
            if i == self.elevator:
                for el in self.floors[i]:
                    if el not in combo:
                        fl.append(el)
            elif i == self.elevator + 1:
                fl.extend(self.floors[i])
                fl.extend(combo)
            else:
                fl.extend(self.floors[i])
            newFloors.append(fl)
        return Solution(self.elevator + 1,newFloors, self, self.step + 1, 'u', combo)
    def moveDown(self, combo):
        newFloors = []
        for i in range(len(self.floors)):
            fl = []
            if i == self.elevator:
                for el in self.floors[i]:
                    if el not in combo:
                        fl.append(el)
            elif i == self.elevator - 1:
                fl.extend(self.floors[i])
                fl.extend(combo)
            else:
                fl.extend(self.floors[i])
            newFloors.append(fl)
        return Solution(self.elevator - 1,newFloors, self, self.step + 1, 'd', combo)


initFloors = [['TG','TM','PG','SG'],['PM','SM'],['HG','HM','RG','RM'],[]]

initSolution = Solution(0, initFloors, None, 0,'u',[])
initSolution.solve()

print(mins)