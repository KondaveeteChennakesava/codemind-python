n = input()
d = '0123456789'
cnt = 0
for i in n:
    if i in d:
        cnt += int(i)
print(cnt)