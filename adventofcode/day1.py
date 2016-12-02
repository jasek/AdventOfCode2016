import math
direction = 'N'
x = 0
y = 0
visited = [(0,0)]

def getDirection(current, rotation):
    dirs = ['N','E','S','W']
    if (rotation == 'R'):
        return {
            'N' : 'E',
            'E' :'S',
            'S' :'W',
            'W' : 'N'
            }.get(current)
    return {
        'N':'W',
        'E':'N',
        'S':'E',
        'W':'S'
        }.get(current)

for s in input().split(", "):
    print(s)
    direction = getDirection(direction, s[:1])
    print(direction)
    if (direction == 'N'):
        for i in range(int(s[1:])):
            y+=1
            if (x,y) in visited:
                print("closest",(x,y),(math.fabs(x)+math.fabs(y)))
            visited.append((x,y))
    elif (direction == 'E'):
        for i in range(int(s[1:])):
            x+=1
            if (x,y) in visited:
                print("closest",(x,y),(math.fabs(x)+math.fabs(y)))
            visited.append((x,y))
    elif (direction == 'S'):        
        for i in range(int(s[1:])):
            y-=1
            if (x,y) in visited:
                print("closest",(x,y),(math.fabs(x)+math.fabs(y)))
            visited.append((x,y))
    else:
        for i in range(int(s[1:])):
            x-=1
            if (x,y) in visited:
                print("closest",(x,y),(math.fabs(x)+math.fabs(y)))
            visited.append((x,y))

print(x,y)
print(math.fabs(x)+math.fabs(y))