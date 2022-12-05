n=int(input())
l=list(map(int,input().split()))
x,y=[],[]
for i in range(n//2):
    x.append(l[i])
for j in range(n//2,n,1):
    y.append(l[j])
#print(*x)
print(abs(sum(y)-sum(x)))