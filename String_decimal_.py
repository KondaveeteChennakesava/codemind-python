for i in range(int(input())):
    n = input()
    res = True
    num = '0123456789'
    for i in n:
        if i not in num:
            res = False
    print(res)