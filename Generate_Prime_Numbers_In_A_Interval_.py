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
b=int(input())
for i in range(a,b+1):
    if pr(i)==True:
        print(i)