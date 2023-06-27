s = input()
x = ''
for i in s:
    if i not in x:
        x += i
if len(x) == len(s):
    print("True")
else:
    print("False")