import time

start = time.time()
lines  = open('input12.txt', 'r').read().splitlines()

def solve(c):
    global lines
    i = 0
    registers = dict()
    registers['a'] = 0
    registers['b'] = 0
    registers['c'] = c
    registers['d'] = 0
    while i < len(lines):
        instr = lines[i].split()
        if instr[0] == 'cpy':
            if instr[1] in ['a','b','c','d']:
                registers[instr[2]] = registers[instr[1]]
            else:
                registers[instr[2]] = int(instr[1])
        elif instr[0] == 'inc':
            registers[instr[1]] +=1
        elif instr[0] == 'dec':
            registers[instr[1]] -=1
        elif instr[0] == 'jnz':
            l = 0
            if instr[1] in ['a','b','c','d']:
                l = registers[instr[1]]
            else:
                l = int(instr[1])
            if l != 0:
                i += int(instr[2])
                i -= 1
        i+=1
    return registers['a']

print('part1:',solve(0))
print('part2:',solve(1))
print('Time elapsed:',time.time() - start)