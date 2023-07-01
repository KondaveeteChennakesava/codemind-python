n = input()
d = '0123456789'
cnt = 0
for i in n:
    if i in d:
        cnt += 1
if cnt>0:
    print(f"Contains {cnt} digit")
else:
    print("Doesn't contain digit")