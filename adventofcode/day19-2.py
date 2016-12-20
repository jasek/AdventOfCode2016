input = 3004953
elfes = []

print(5 // 2)

def getNextNumber(i):
    lenght = len(elfes) 
    if i + 1 >= lenght:
        return i + 1 - lenght
    return i + 1


def getAcrossElf(i):
    lenght = len(elfes) 
    hl = lenght // 2
    if i + hl >= lenght:
        return i - (lenght - hl)
    return  i + hl



for i in range(input):
    elfes.append(i + 1)

i = 0
while len(elfes) > 1:
    across = getAcrossElf(i)
    #print(i,elfes)
    print((input - len(elfes)) * 100 / input)
    #next = getNext(i)
    #elfes[i] = elfes[i] + elfes[next]
    elfes.pop(across)
    if across < i:
        i = getNextNumber(i) - 1
    else:
        i = getNextNumber(i)
print(elfes)