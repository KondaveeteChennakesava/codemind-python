n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
for i in range(b,a,-1):
    if i in l:
        print(i)
        break
else:
    print(-1)