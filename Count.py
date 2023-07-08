n = int(input())
l = list(map(int,input().split()))
ol,el = [],[]
for i in l:
    if i%2:
        ol.append(i)
    else:
        el.append(i)
print(len(el),len(ol))