n=int(input())
sq=n**2
su=0
while sq>0:
    r=sq%10
    sq=sq//10
    su+=r
if su==n:
    print("Neon Number")
else:
    print("Not Neon Number")