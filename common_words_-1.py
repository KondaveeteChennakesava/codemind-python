n1 = input().lower()
n2 = input().lower()
cnt = 0
for a in n1.split():
    for b in n2.split():
        if a == b:
            cnt += 1
print(cnt)