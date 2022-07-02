a=input()
k=input()
c=0
for i in a:
    if i==k:
        print("True")
        c+=1
        print(a.index(i))
        break
else:
    if c==0:
        print("False")