n,m = map(int,input().split())
m1,m2 = [],[]
for i in range(n):
    m1.append(list(map(int,input().split())))
l = []
for i in m1:
    l.append(sum(i))
print(max(l))