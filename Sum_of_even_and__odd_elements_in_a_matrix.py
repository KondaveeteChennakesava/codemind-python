n,m = map(int,input().split())
m1 = []
for i in range(n):
    m1.append(list(map(int,input().split())))
ec,oc = 0,0
for i in range(n):
    for j in range(m):
        if m1[i][j] % 2 == 0:
            oc += m1[i][j]
        else:
            ec += m1[i][j]
print(oc,ec)