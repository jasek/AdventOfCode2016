import hashlib
import string

#wrong implementation

hashnumbers = set()
salt = 'abc'
limit = 64

candidates = dict()

triplets = []
for l in string.ascii_lowercase:
    triplets.append(l * 3)
for i in range(10):
    triplets.append(str(i) * 3)

def hashs(s):
    for i in range(1):
        m = hashlib.md5()
        m.update(s.encode('utf-8'))
        s = m.hexdigest()
    return s

def solve():
    maximus = 0
    i = 0
    while True:        
        test = salt + str(i)
        #test = test
        hash = hashs(test)
        #print(hash)
        keyslist = list(candidates.keys())
        if len(hashnumbers) < limit:
            cand = []
            for t in triplets:
                if t in hash:
                    cand.append(t[0:1])
                    break
            if len(cand) > 0:
                maximus = i
                candidates[i] = cand
                #print(candidates)
        for c in keyslist:
            if c >= i - 1000:
                #print(candidates[c])
                for cs in list(candidates[c]):
                    if cs * 5 in hash:
                        hashnumbers.add(c)
                        print(len(hashnumbers),c)
                        del candidates[c]
                        if len(candidates) ==0:
                            return
                        break
            else:
                del candidates[c]
                if len(candidates) ==0:
                    return


        i+=1
solve()
hashlist = list(hashnumbers)
hashlist.sort()
print(hashlist, len(hashnumbers))
print(max(hashnumbers))
for h in range(len(hashlist)):
    print(h+1,hashlist[h],hashs(salt+str(hashlist[h])))