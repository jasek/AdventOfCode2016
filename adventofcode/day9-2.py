def decompress(code):
    i = 0
    res = 0
    while i < len(code):
        if code[i] == '(':
            end = code.find(')',i)
            x,y = [int(x) for x in code[i+1:end].split('x')]
            i = end +1 +x
            res+= decompress(code[end +1:i]) * y
        else:
            res+=1
            i+=1
    return res
print(decompress(open('input9.txt', 'r').read()))