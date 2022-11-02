a=int(input())
l=list(map(int,input().split()))
e=int(input())
for i in range(len(l)):
    if e in l:
        print("True")
        break
    else:
        print("False")
        break