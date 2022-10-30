a=int(input())
asq=a**2
arev=0
while a>0:
    r=a%10
    a//=10
    arev=arev*10+r
arevsq=arev**2
arevsqrev=0
while arevsq>0:
    r=arevsq%10
    arevsq//=10
    arevsqrev=arevsqrev*10+r
if asq==arevsqrev:
    print("True")
else:
    print("False")