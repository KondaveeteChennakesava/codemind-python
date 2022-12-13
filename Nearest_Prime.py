from math import *
def pr(a):
    if a>0:
        for i in range(2,int(sqrt(a)+1)):
            if a%i==0:
                return False
    elif a==1:
        return False
    return True

for i in range(int(input())):
    a=int(input())
    #print(a)
    for k in range(a,99999999):
        if pr(k)==True:
            gp=k
            break
    for j in range(a,-1,-1):
        if pr(j)==True:
            sp=j
            break
    fc=gp-a
    bc=a-sp
    if fc>=bc:
        print(sp)
    else:
        print(gp)