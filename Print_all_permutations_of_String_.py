from itertools import permutations
n = input()
for i in permutations(n):
    print(''.join(i))