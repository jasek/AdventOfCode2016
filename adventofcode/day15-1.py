import time

start = time.time()
discs = []

lines  = open('input15.txt', 'r').read().splitlines()


def addToDisc(disc, i):
    discs[disc][1] = (discs[disc][1] + i) % discs[disc][0]
    return discs[disc][1]

for i in range(len(lines)):
    el = lines[i].split()
    discs.append([int(el[3]), int(el[11][:-1])])
for i in range(len(discs)):
    addToDisc(i,i+1)

inc = 5
for i in range(len(discs)):
    addToDisc(i,5)
while True:
    inc += 19
    #print
    #print(inc)
    fin = True
    for i in range(len(discs)):
        r = addToDisc(i,19)
        if r != 0:
            fin = False
    #print(discs)
    if fin:
        break


print(discs)
print(inc)

end = time.time()
print('Time elapsed:',(end - start))