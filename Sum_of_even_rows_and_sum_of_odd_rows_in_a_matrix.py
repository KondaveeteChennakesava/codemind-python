n,m = map(int,input().split())
m1 = []
for i in range(n):
    m1.append(list(map(int,input().split())))
ec,oc = 0,0
for i in range(n):
    for j in range(m):
        if i%2 == 0:
            ec += m1[i][j]
        else:
            oc += m1[i][j]
print(ec,oc)