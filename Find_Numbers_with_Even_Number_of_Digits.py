def ev(a):
    c=0
    while a>0:
        r=a%10
        a//=10
        c+=1
    if c%2==0:
        return True
    else:
        return False
a=int(input())
l=list(map(int,input().split()))
cnt=0
for i in l:
    if ev(i)==True:
        cnt+=1
print(cnt)