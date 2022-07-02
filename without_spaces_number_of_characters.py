v=input()
r=0
for k in range(0,len(v)):
    if((ord(v[k])!=32)):
        r+=1
print(r)