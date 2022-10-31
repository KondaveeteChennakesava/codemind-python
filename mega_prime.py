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
a=int(input())
if pr(a)==True:
    p,c=0,0
    while a>0:
        r=a%10
        a//=10
        c+=1
        if pr(r)==True:
            p+=1
    if c==p:
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")