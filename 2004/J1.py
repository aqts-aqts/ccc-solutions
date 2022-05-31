import sys
input = sys.stdin.readline
print = lambda *x, sep=' ', end='\n': sys.stdout.write(sep.join(map(str, x)) + end)
n = int(input())
size = 0
i = 1
while i ** 2 <= n:
    size += 1
    i += 1
print('The largest square has side length', size, end='.\n')