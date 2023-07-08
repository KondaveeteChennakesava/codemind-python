n = int(input())
l = list(map(int,input().split()))
k = l[n//2:n][::-1]
for i in range(n//2):
    k.append(l[i])
print(*k)