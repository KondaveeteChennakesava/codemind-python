s1=input()
s2=input()
n=s1.lower()
m=s2.lower()
s3=n.split()
s4=m.split()
for i in s4:
    if i in s3:
        print(i,end=' ')
    