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
def pa(a):
    rev=0
    temp=a
    while a>0:
        r=a%10
        a//=10
        rev=rev*10+r
    if rev==temp:
        return True
    else:
        return False

a=int(input())
for i in range(a+1,100000):
    if pr(i)==True and pa(i)==True:
        print(i)
        break