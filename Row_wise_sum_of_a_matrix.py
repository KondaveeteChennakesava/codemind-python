n,m = map(int,input().split())
m1 = []
for i in range(n):
    m1.append(list(map(int,input().split())))
for i in m1:
    print(sum(i),end=' ')