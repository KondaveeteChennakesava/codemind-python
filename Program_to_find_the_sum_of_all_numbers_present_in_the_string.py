n = input()
cnt = 0
for i in n:
    if i.isdigit():
        cnt += int(i)
print(cnt)