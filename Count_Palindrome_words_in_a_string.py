def pl(a):
    a = a.lower()
    k = a[::-1]
    if a == k:
        return True
    return False
n = input().split()
cnt = 0
for i in n:
    if pl(i):
        cnt += 1
print(cnt)
#print(pl('Madam'))