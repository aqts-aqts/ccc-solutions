import sys
import time
from itertools import permutations
input = sys.stdin.readline

def solve(n1, n2, s):
    first = list(set(n1[0] + n2[0] + s[0]))
    letters = list(set(n1 + n2 + s))
    letters += ['!'] * (10 - len(letters))
    perms = permutations(letters)
    for perm in perms:
        num1 = n1; num2 = n2; sums = s
        isFirst = False
        for f in first:
          if perm[0] == f: isFirst = True; break
        if isFirst: continue
        for i in range(len(perm)):
            if perm[i] == '!': continue # iterate through each of the numbers instead of running replace() on every iteration
            num1 = num1.replace(perm[i], str(i)); num2 = num2.replace(perm[i], str(i)); sums = sums.replace(perm[i], str(i))
        if int(num1) + int(num2) == int(sums):
            return [num1, num2, sums]

for i in range(int(input())):
    n1 = input().strip()
    n2 = input().strip()
    s = input().strip()
    now = time.time()
    print('\n'.join(solve(n1, n2, s)))
    end = time.time() - now
    print(end)