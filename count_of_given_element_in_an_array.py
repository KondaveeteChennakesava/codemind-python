a=int(input())
l=list(map(int,input().split()))
e=int(input())
c=0
for i in range(len(l)):
    if e==l[i]:
        c+=1
print(c)