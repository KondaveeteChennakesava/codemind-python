def cnt(a):
    c=0
    while a>0:
        r=a%10
        a//=10
        c+=1
    return c
n=int(input())
l=list(map(int,input().split()))
k=min(l)
cn=0
for i in l:
    if cnt(k)==cnt(i):
        cn+=1
print(cn)