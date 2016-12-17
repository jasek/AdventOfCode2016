import time

start = time.time()
part1 = 272
part2 = 35651584
randomdata = '11110010111001001'

def solve(lenght, randomdata):     
    while len(randomdata) < lenght:
        b = randomdata
        b = b[::-1]
        b = b.replace('1','2')
        b = b.replace('0','1')
        b = b.replace('2','0')
        randomdata += '0'
        randomdata += b
        
    if len(randomdata) > lenght:
        randomdata = randomdata[:lenght]
    checksum = randomdata
    while True:
        rand2 = checksum
        checksum = ''
        for i in range(0,len(rand2),2):
            if rand2[i:i + 2][:1] == rand2[i:i + 2][1:]:
                checksum += '1'
            else:
                checksum += '0'
        if len(checksum) % 2 == 1:
            return checksum

print('part1:',solve(part1,randomdata))
print('part2:',solve(part2,randomdata))
print('Time elapsed:',(time.time() - start))