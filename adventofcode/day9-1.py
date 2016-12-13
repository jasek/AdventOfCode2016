code = open('input9.txt', 'r').read()
res = ''

i = 0
while i < len(code):
    if code[i] == '(':
        end = code.find(')',i)
        x,y = [int(x) for x in code[i+1:end].split('x')]
        print(x,y)
        i = end +1
        print(i,code[i])
        for j in range(y):
            res+=code[i:i+x]
            #print(code[i:i+x])
        print(i,'+',x)
        i += x
    else:
        print(i,'+1')
        res+=code[i]
        i+=1


print(res, len(res))


