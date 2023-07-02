for i in range(int(input())):
    n = int(input())
    s = input()
    k = ''
    for i in s:
        if s.count(i) == 1:
            k += i
    if k == '':
        print(-1)
    else:
        print(k[0])