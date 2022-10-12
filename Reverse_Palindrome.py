def res(n):
    rev=0
    temp=n
    while n>0:
        d=n%10
        n=n//10
        rev=rev*10+d
    return rev
n=int(input())
sum=0
while True:
    sum=n+res(n)
    if sum==res(sum):
        print(sum)
        break
    else:
        n=sum
        continue