fn = 1364
m = []
PIXON ='\u2588'
PIXOFF = '\u2592'
def calculate(x, y):
    return x * x + 3 * x + 2 * x * y + y + y * y + fn

def evenBinaryZeros(i):
    return 0 if bin(i)[2:].count('1') % 2 == 0 else 1


def createMatrix(size):
    for i in range(size):
        row = []
        for j in range(size):
            row.append(evenBinaryZeros((calculate(j,i))))
        m.append(row)

def printMatrix():
    fr = '   '
    fr2 = '   '
    for i in range(len(m)):
        fr += str(i)[-1:]
        fr2 += str(i).zfill(2)[:1]
    print(fr2)
    print(fr)
    for l in range(len(m)):
        ln = ''.join(str(m[l]))
        if l == 39:
            ln = ln[:31] + 'O' + ln[32:]
        print(str(l).zfill(2) + ' ' + ln)

def export():
    for l in m:
        print(';'.join(l))

createMatrix(50)
print(m)

printMatrix()

print(calculate(0,2))
print(bin(calculate(0,2)))
print(evenBinaryZeros(calculate(1,1)))