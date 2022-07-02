s=input()
s=s.split()
k=0
for x in s:
    if(x.casefold()==x.casefold()[::-1]):
        k+=1
print(k)        
