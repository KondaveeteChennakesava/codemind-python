n = input()
m ='a'
for i in n:
    if ord(i)>ord(m):
        m = i
print(m)