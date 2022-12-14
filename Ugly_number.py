a=int(input())
while a%2==0 or a%3==0 or a%5==0:
    if a%2==0:
        a//=2
    elif a%3==0:
        a//=3
    elif a%5==0:
        a//=5
if a==1:
    print("Ugly Number")
else:
    print("Not Ugly Number")