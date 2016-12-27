lines = open('input22.txt', 'r').read().splitlines()

pairs = []
nodes = []

def isViableInOrder(node1, node2):
    return node1[2] > 0 and node1[2] <= node2[3]

def isPairViable(node1, node2):
    if isViableInOrder(node1, node2):
        return True
    elif isViableInOrder(node2, node1):
        return True
    else:
        return False

for l in range(2,len(lines)):
    node = lines[l].split()
    nodes.append((node[0],int(node[1][:-1]),int(node[2][:-1]),int(node[3][:-1]),int(node[4][:-1])))

for i in range(len(nodes)):
    for j in range(i + 1, len(nodes)):
        #print(nodes[i],nodes[j])
        if isPairViable(nodes[i],nodes[j]):
            pairs.append((nodes[i],nodes[j]))

print('part1',len(pairs))