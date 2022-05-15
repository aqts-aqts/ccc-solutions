import sys
print = sys.stdout.write
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    print('*' * n)
    print('x' * n)
    print('*' * n + '\n')
for _ in range(n):
    print(' ' * n)
    print('x' * n)
    print('x' * n + '\n')
for _ in range(n):
    print('*' * n)
    print(' ' * n)
    print('*' * n + '\n')