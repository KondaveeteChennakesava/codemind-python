for i in range(int(input())):
    n = input()
    r = n[::-1]
    if n != r:
        print("NO")
    else:
        k = ''
        if len(n)%2 == 0:
            k += 'EVEN'
        else:
            k += 'ODD'
        print("YES",k)