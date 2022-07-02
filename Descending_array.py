n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(len(a)-1):
    if(a[i]<a[i+1]):
        print('no')
        c+=1
        break
if(c==0):
    print('yes')