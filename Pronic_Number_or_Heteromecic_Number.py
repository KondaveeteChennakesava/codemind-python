a=int(input())
c=0
for i in range(1,a+1):
    if a%i==0:
        if i*(i+1)==a:
            c=1
if c==1:
    print("YES")
else:
    print("NO")