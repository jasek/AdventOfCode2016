input = 3004953
elfes = dict()

def getNextNumber(i):
    if i + 1 > input:
        return i + 1 - input
    return i + 1

def getNext(i):
    res = getNextNumber(i)
    while res not in elfes:
        res = getNextNumber(res)
    return res

for i in range(1,input + 1):
    elfes[i] = 1

i = 1
while len(elfes) > 1:
    print(len(elfes))
    next = getNext(i)
    elfes[i] = elfes[i] + elfes[next]
    elfes.pop(next)
    i = getNext(i)
print(elfes)