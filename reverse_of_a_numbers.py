a=int(input())
res=0
while a>0:
    r=a%10
    a//=10
    res=res*10+r
print(res)