a=int(input())
l=[]
temp=a
while a>0:
    r=a%10
    a//=10
    l.append(r)
l.reverse()
ts=0
for i in range(len(l)):
    ts+=l[i]**(i+1)
    #print(ts)
#print(a,temp,ts)
if ts==temp:
    print(True)
else:
    print(False)