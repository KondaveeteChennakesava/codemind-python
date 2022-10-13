import math
def fun(a):
    for i in range(int(a)):
        c=1
        r=i*i
        if r==a:
            return True
            c=0
            break
    if c==1:
        return False
a=int(input())
n=fun(a)
print(n)