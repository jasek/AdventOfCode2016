import time
import fractions

start = time.time()
discs = []
biggestdisk = (0,0)
lines = open('input15.txt', 'r').read().splitlines()

def addToDisc(disc, i):
    discs[disc][1] = (discs[disc][1] + i) % discs[disc][0]
    return discs[disc]
def lcm(num1, num2):
    return int((num1 * num2) / fractions.gcd(num1 , num2))

for i in range(len(lines)):
    el = lines[i].split()
    discs.append([int(el[3]), int(el[11][:-1])])
for i in range(len(discs)):
    addToDisc(i,i + 1)
for disc in discs:
    if disc[0] > biggestdisk[0]:
        biggestdisk = disc

step = biggestdisk[0]
steps = 0
# set biggest disk in good position
inc = biggestdisk[0] - biggestdisk[1]
for i in range(len(discs)):
    addToDisc(i,inc)
while True:
    steps+=1
    inc +=step
    fin = True
    for i in range(len(discs)):
        dis = addToDisc(i,step)
        r = dis[1]
        if r != 0:
            fin = False
        else:
            step = lcm(step,dis[0])
    if fin:
        break

print('result',inc)
print('steps',steps)
print('Time elapsed:',(time.time() - start))