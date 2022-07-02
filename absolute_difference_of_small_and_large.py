n=list(map(str,input().split()))
d=[]
for i in n:
    d.append(abs(ord(min(i))-ord(max(i))))
for i in d:
    print(i,end=' ')