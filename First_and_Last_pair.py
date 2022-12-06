n=int(input())
l=list(map(int,input().split()))
k=[]
if n%2==0:
    for i in range(n//2):
        k.append(l[i])
        k.append(l[-i-1])
elif n%2:
    for i in range(n//2):
        k.append(l[i])
        k.append(l[-i-1])
    else:
        k.append(l[n//2])
        k.append(0)
print(*k)
        