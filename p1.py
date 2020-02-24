l=eval(input())
lst=l.copy()
a=lst[0]
out=[a]
while lst:
    for i in lst.copy():
        if a[-1]==i[0]:
            a=i
            out.append(i)
            lst.remove(i)
out.pop()
print(out)
    
                    
