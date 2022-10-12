def gcd(a,b):
    if b>a:
        a,b=b,a
    r=a%b
    if r!=0:
        gcd(b,r)
    elif r==0:
        print(b)

a,b=map(int,input().split())
if a==0:
    print(b)
elif b==0:
    print(a)
else:
    gcd(a,b)
    

