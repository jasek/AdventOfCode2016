lines  = open('input10.txt', 'r').read().splitlines()


LOW = 6
HIGH = 11
LOWT = 5
HIGHT = 10
C1 = 61
C2 = 17

bots = dict()
output = dict()
instructions = dict()
for l in lines:
    if l.startswith('value'):
        print(l)
        val = int(l[6:l.find(' ',6)])
        bot = int(l[l.find('bot')+4:])
        print(val, bot)
        if (bot in bots):
            bots[bot].append(val)
        else:
            bots[bot] = [val]
for l in lines:
    if l.startswith('bot'):
        print(l)
        line = l.split(' ')
        bot = int(line[1])
        instructions[bot] = line

print(bots)

bot = 0
while True:
    breaking = True
    for b in bots:
        val = bots[b]
        if len(bots[b]) == 2:
            bot = b
            #print(bot, bots[b])
            breaking = False
            break
    if breaking:
        break

    if C1 in bots[bot] and C2 in bots[bot]:
        print('res',bot)
        #break
    instr = instructions[bot]
    low = int(instr[LOW])
    high = int(instr[HIGH])
    if instr[LOWT] == 'output':
        if (low in output):
            output[low].append(min(bots[bot]))
        else:
            output[low] = [min(bots[bot])]
    else:
        if (low in bots):
           bots[low].append(min(bots[bot]))
        else:
           bots[low] = [min(bots[bot])]
    if instr[HIGHT] == 'output':
        if (high in output):
            output[high].append(max(bots[bot]))
        else:
            output[high] = [max(bots[bot])]
    else:
        if (high in bots):
            bots[high].append(max(bots[bot]))
        else:
            bots[high] = [max(bots[bot])]
    bots[bot] = []

print('res2',output[0][0]*output[1][0]*output[2][0])

   