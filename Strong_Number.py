def fact(a):
    if a==1 or a==0:
        return a
    else:
        return a*fact(a-1)
n=int(input())
temp=n
ts=0
while n>0:
    r=n%10
    n//=10
    ts+=fact(r)
if ts==temp:
    print("The number",temp,"is a strong number")
else:
    print("The number",temp,"is not a strong number")