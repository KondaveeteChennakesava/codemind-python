a=int(input())
k=[]
while a>0:
    r=a%10
    a//=10
    k.append(r)
print(max(k))