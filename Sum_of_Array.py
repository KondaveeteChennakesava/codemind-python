a=int(input())
l=list(map(int,input().split()))
oc=0
for i in range(len(l)):
    oc+=l[i]
print(oc)