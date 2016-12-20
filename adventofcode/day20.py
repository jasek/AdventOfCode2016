lines = open('input20.txt', 'r').read().splitlines()
ranges = []
allowed = []

for l in lines:
    ranges.append([int(x) for x in  l.split('-')])
ranges.sort()
min = 0
allowednumber = 0
for range in ranges:
    if range[0] <= min + 1 and range[1] >= min + 1:
        min = range[1] 
    elif range[0] > min +1:
        allowed.append([min+1,range[0]-1])
        min = range[1]
#print(ranges)
#print('all',allowed)

for all in allowed:
    allowednumber += all[1]-all[0]+1
print('result 1:',allowed[0][0])
print('result 2:',allowednumber)