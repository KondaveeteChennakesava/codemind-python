a=int(input())
b=int(input())
s,d=0,0
for i in range(1,a+1):
    if a%i==0:
        s+=i
for j in range(1,b+1):
    if b%j==0:
        d+=j
if s==d:
    print("Amicable")
else:
    print("Not Amicable")