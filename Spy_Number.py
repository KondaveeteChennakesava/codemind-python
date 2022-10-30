a=int(input())
s,p=0,1
while a>0:
    r=a%10
    a=a//10
    s+=r
    p*=r
if s==p:
    print("Spy Number")
else:
    print("Not Spy Number")