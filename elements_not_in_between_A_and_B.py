n=int(input())
L=[int(i) for i in input().split(" ")]
A,B=[int(i) for i in input().split(" ")]
count=0
for ele in L:
    if ele<A or ele>B:
        print(ele,end=" ")
        count=count+1
if count==0:
    print(-1)