import sys
input = sys.stdin.readline
print = lambda *x, sep=' ', end='\n': sys.stdout.write(sep.join(map(str, x)) + end)
x = int(input())
y = int(input())
for i in range(x, y + 1, 60):
    print('All positions change in year', str(i))