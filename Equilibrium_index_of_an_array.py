for t in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    e1,e2 = 0,0
    x,y,res = [],[],-1
    for i in range(n):
        e1 += l[i]
        x.append(e1)
        e2 += l[n-i-1]
        y.append(e2)
    y.reverse()
    for i in range(n):
        if x[i] == y[i]:
            res = i
    print(res)