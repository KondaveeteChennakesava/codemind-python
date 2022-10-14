def pl(a):
    rev=0
    temp=a
    while a>0:
        r=a%10
        a//=10
        rev=rev*10+r
    if rev!=temp:
        return False
    return True
a=int(input())
b=int(input())
for i in range(a,b+1):
    if pl(i)==True:
        print(i,end=" ")