n,m = map(int,input().split())
m1,m2 = [],[]
for i in range(n):
    m1.append(list(map(int,input().split())))
for i in range(m):
    tl = []
    for j in range(n):
        tl.append(m1[j][i])
    m2.append(tl)
for i in m2:
    print(sum(i),end=' ')