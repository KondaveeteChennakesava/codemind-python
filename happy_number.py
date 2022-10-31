def hp(a):
    s=0
    while a>0:
        r=a%10
        a//=10
        s+=r**2
    if s>9:
        return hp(s)
    elif s==1 or s==7:
        return True
    else:
        return False


a=int(input())
if hp(a)==True:
    print("True")
else:
    print("False")