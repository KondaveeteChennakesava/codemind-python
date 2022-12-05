n=int(input())
l=list(map(int,input().split()))
#print(*l)
for i in range(n-1,-1,-1):
    if l[i]%2:
        print(i)
        break