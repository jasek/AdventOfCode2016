import time

start = time.time()
lines = open('input23.txt', 'r').read().splitlines()


registers = dict()
registers['a'] = 12
registers['b'] = 0
registers['c'] = 0
registers['d'] = 0


def read(a):
    if a in registers:
        return registers[a]
    return int(a)


def solve(c):
    global lines
    i = 0

    while i < len(lines):
        instr = lines[i].split()
        #print(registers['a'],registers['b'],registers['c'],registers['d'])
        #print(instr)
        if instr[0] == 'cpy':
            registers[instr[2]] = read(instr[1])
        elif instr[0] == 'inc':
            registers[instr[1]] +=1
        elif instr[0] == 'dec':
            registers[instr[1]] -=1
        elif instr[0] == 'jnz':
            l = 0
            l = read(instr[1])
            if l != 0:
                i += read(instr[2])
                i -= 1        
        elif instr[0] == 'tgl':
            forchange = i + read(instr[1])
            if forchange < len(lines):
                instrchange = lines[forchange].split()
                if instrchange[0] == 'inc':
                    instrchange[0] = 'dec'
                elif instrchange[0] == 'dec' or instrchange[0] == 'tgl':
                    instrchange[0] = 'inc'
                elif  instrchange[0] == 'jnz':
                    instrchange[0] = 'cpy'
                else:
                    instrchange[0] = 'jnz'
                lines[forchange] = ' '.join(instrchange)
        i+=1
        #print(instr)
    return registers['a']
print('part1:',solve(0))
print(registers['a'],registers['b'],registers['c'],registers['d'])
print('Time elapsed:',time.time() - start)
