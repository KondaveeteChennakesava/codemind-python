def fact(a):
    if a==1:
        return a
    else:
        return a*fact(a-1)
for i in range(int(input())):
    a=int(input())
    print(fact(a))