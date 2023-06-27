n,m = map(int,input().split())
m1 = []
for i in range(n):
    m1.append(list(map(int,input().split())))
cnt = 0
for i in range(n):
    for j in range(m):
        cnt += m1[i][j]
print(cnt)