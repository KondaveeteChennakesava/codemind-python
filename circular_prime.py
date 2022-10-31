import math
def pr(a):
    if a>1:
        for i in range(2,int(math.sqrt(a)+1)):
            if a%i==0:
                return False
                break
    elif a==1:
        return False
    return True
def rev(a):
    res=0
    while a>0:
        r=a%10
        a=a//10
        res=res*10+r
    return res
a=int(input())
b=rev(a)
if pr(a)==True and pr(b)==True:
    print("circular prime")
elif pr(a)==True and pr(b)!=True or pr(a)!=True and pr(b)==True:
    print("prime but not a circular prime")
else:
    print("not prime")