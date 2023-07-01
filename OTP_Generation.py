n = input()
a = ''
for i in n:
    if int(i)%2 == 0:
        pass
    else:
        a += str(int(i)**2)
print(a)