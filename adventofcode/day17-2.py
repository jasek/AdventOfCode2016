import hashlib
import time

start = time.time()
open = {'b','c','d','e','f'}
input = 'hhhxzeay'
solutions = []

def getDoorsState(x,y,path):
    res = []
    m = hashlib.md5()
    m.update((input + path).encode('utf-8'))
    hash = m.hexdigest()
    res.append(False if y == 0 else hash[0] in open)
    res.append(False if y == 3 else hash[1] in open)
    res.append(False if x == 0 else hash[2] in open)
    res.append(False if x == 3 else hash[3] in open)
    return res

def solve():
    queue = [(0,0,'')]
    while len(queue) > 0:
        q = queue.pop(0)
        if q[0] == 3 and q[1] == 3:
            solutions.append(q)
        else:
            doors = getDoorsState(q[0],q[1],q[2])
            if doors[0]:
                queue.append((q[0] , q[1] - 1, q[2] + 'U'))
            if doors[1]:
                queue.append((q[0] , q[1] + 1, q[2] + 'D'))
            if doors[2]:
                queue.append((q[0] - 1, q[1] , q[2] + 'L'))
            if doors[3]:
                queue.append((q[0] + 1 , q[1], q[2] + 'R'))

solve()
print(len(solutions[-1][2]))
end = time.time()
print('Time elapsed:',(end - start))