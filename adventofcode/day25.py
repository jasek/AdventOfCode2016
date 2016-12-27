import time

start = time.time()
lines = open('input25.txt', 'r').read().splitlines()


registers = dict()
registers['a'] = 0
registers['b'] = 0
registers['c'] = 0
registers['d'] = 0

lasta = 0

def read(a):
    if a in registers:
        return registers[a]
    return int(a)


def solve(c):
    global lines, lasta
    while True:
        i = 0
        last = 1
        lasta = lasta + 1
        registers['a'] = lasta
        test = 0
        while i < len(lines):
            instr = lines[i].split()
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
            elif instr[0] == 'out':
                print(read(instr[1]))
                code = read(instr[1])
                if last == 1 and code != 0:
                    print('old a', lasta)
                    break
                if last == 0 and code != 1:
                    print('old a', lasta)
                    break
                test +=1
                if test > 1000:
                    print('working', lasta)
                    return lasta
                last = code

            i+=1
    return registers['a']
print('part1:',solve(0))
print(registers['a'],registers['b'],registers['c'],registers['d'])
print('Time elapsed:',time.time() - start)
