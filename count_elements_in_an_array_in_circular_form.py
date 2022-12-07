n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(n):
    if i==0 and (l[-1]%2 and l[1]%2==0) or (l[-1]%2==0 and l[1]%2):
        c+=1
    if i==n-1 and (l[0]%2 and l[n-2]%2==0) or (l[0]%2==0 and l[n-2]%2):
        c+=1
for i in range(1,n-1):
    if (l[i-1] %2==0 and l[i+1]%2) or (l[i-1]%2 and l[i+1]%2==0):
        c+=1
print(c)