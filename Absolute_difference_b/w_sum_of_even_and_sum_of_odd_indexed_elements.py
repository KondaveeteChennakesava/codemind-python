a=int(input())
l=list(map(int,input().split()))
oc,ec=0,0
for i in range(len(l)):
    if i%2:
        oc+=l[i]
    else:
        ec+=l[i]
print(abs(ec-oc))