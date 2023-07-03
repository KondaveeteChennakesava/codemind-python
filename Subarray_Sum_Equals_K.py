a,b = map(int,input().split())
l = list(map(int,input().split()))
sr = []
cnt = 0
for i in range(len(l)):
    for j in range(i,len(l)):
        if sum(l[i:j+1]) == b:
            cnt += 1
print(cnt)