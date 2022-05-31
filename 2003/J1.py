import sys
sys.setrecursionlimit(int(1e9))
input = sys.stdin.readline
print = lambda *x, sep=' ', end='\n': sys.stdout.write(sep.join(map(str, x)) + end)
t = int(input())
s = int(input())
h = int(input())
trident = ('*' + ' ' * s) * 2 + '*'
for _ in range(t): print(trident)
print('*' * (len(trident)))
for _ in range(h):
    print(' ' * (len(trident) // 2) + '*')