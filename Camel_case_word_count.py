n = input()
cnt = 0
for i in range(len(n)):
    if (ord(n[i])>=65 and ord(n[i])<=91):
        cnt += 1
if ord(n[0])>91:
    cnt += 1
print(cnt)