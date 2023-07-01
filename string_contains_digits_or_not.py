for i in range(int(input())):
    n = input()
    d = '0123456789'
    cnt = 0
    for i in n:
        if i in d:
            cnt = 1
            break
    if cnt == 1:
        print("Yes")
    else:
        print("No")