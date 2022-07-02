a=input()
b=''
count=0
for i in a:
    if i!=' ':
        b=b+i
b=b.lower()
c=set(b)
for j in c:
    count+=1
print(count)