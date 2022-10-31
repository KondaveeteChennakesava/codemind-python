a=int(input())
l=[]
c=1
while a>0:
    r=a%10
    a=a//10
    if r in l:
        print("Not Unique Number")
        c=0
        break
    l.append(r)
if c==1:
    print("Unique Number")