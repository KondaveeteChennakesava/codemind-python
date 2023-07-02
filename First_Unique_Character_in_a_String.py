n = input().lower()
k = -1
for i in range(len(n)):
    if n.count(n[i]) == 1:
        k = i
        break
print(k)