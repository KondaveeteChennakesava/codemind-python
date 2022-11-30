n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
s=0
for i in range(a,b+1):
    if i in l:
        s+=i
print(s)