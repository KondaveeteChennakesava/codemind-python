def sr(l):
    a = l.copy()
    a.sort()
    if l == a:
        return True
    return False

n,m = map(int,input().split())
m1,m2 = [],[]
for i in range(n):
    m1.append(list(map(int,input().split())))
for i in range(m):
    l = []
    for j in range(n):
        l.append(m1[j][i])
    m2.append(l)
#print(m2)
cnt = 0
for i in m2:
    if sr(i) == True:
        cnt += 1
print(cnt)