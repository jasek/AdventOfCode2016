from collections import Counter

res = ''
inpt = []
while True:
    l= input()
    if l=='':
        break
    inpt.append(l)

columns = []
for i in range(len(inpt[0])):
    columns.append('')

for l in inpt:
    for i in range(len(l)):
        columns[i] += l[i:i+1]

for c in columns:
    x = Counter(c)
    x = sorted(x.items(), key=lambda i: i[1], reverse=False)
    x = x[0]
    res += x[0]
print("Result:",res)
          