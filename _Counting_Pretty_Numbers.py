def pr(a):
    r=a%10
    if r==2 or r==3 or r==9:
        return True
    else:
        return False
for i in range(int(input())):
    a,b=map(int,input().split())
    c=0
    for j in range(a,b+1):
        if pr(j)==True:
            c+=1
    print(c)