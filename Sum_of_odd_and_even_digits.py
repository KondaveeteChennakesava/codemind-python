a=int(input())
l=list(map(int,input().split()))
od,ev=0,0
for i in range(a):
    if i%2:
        od+=l[i]
    else:
        ev+=l[i]
if abs(od-ev)==0:
    print("YES")
else:
    print("NO")