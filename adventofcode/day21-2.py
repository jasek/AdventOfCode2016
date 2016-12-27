lines = open('input21.txt', 'r').read().splitlines()
input = 'fbgdceah'
LEN = len(input)

def rotatebased(inpt,x):
    pos = inpt.index(x)
    if pos >= 4:
        pos+=1
    pos+=1
    pos = pos % LEN
    return inpt[LEN - pos:] + inpt[:LEN - pos]

def move(inpt,x,y):
    let = inpt[x]
    inpt = inpt[:x] + inpt[x + 1:]
    inpt = inpt[:y] + let + inpt[y:]
    return inpt

def reversedrotatebased(inpt,x):
    for i in range(LEN):
        rotated = inpt[LEN - i:] + inpt[:LEN - i]
        rotated2 = rotatebased(rotated,x)
        if rotated2 == inpt:
            return inpt[LEN - i:] + inpt[:LEN - i]

for l in lines[::-1]:
    before = input
    instr = l.split()
    if instr[0] == 'swap':
        if instr[1] == 'position':
            x = int(instr[2])
            y = int(instr[5])
            xl = input[x]
            inpl = list(input)
            inpl[x] = inpl[y]
            inpl[y] = xl
            input = ''.join(inpl)
        else:
            x = instr[2]
            y = instr[5]
            input = input.replace(x, '_')
            input = input.replace(y, x)
            input = input.replace('_', y)
    elif instr[0] == 'rotate':
        if instr[1] == 'based':
            input = reversedrotatebased(input, instr[6])
        else:
            mv = 0
            if instr[1] == 'right':
                mv = LEN - int(instr[2])
            else:
                mv = int(instr[2])
            input = input[LEN - mv:] + input[:LEN - mv]
    elif instr[0] == 'reverse':
        x = int(instr[2])
        y = int(instr[4])
        input = input[:x] + input[x:y + 1][::-1] + input[y + 1:]
    elif instr[0] == 'move':
        x = int(instr[2])
        y = int(instr[5])
        input = move(input,y,x)
    print(before,';',input,';',instr)
    
