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
c=a+b
for i in range(c+1,1100):
    if pr(i)==True:
        print(i-c)
        break