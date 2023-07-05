def sr(l):
    a = l.copy()
    a.sort()
    b = l.copy()
    b.sort(reverse = True)
    if l == a or l == b:
        return True
    return False



n,m = map(int,input().split())
m1 = []
for i in range(n):
    m1.append(list(map(int,input().split())))
cnt = 0
for i in m1:
    if sr(i) == True:
        cnt += 1
print(cnt)