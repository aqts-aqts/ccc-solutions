import sys
input = sys.stdin.readline
print = lambda *x, sep=' ', end='\n': sys.stdout.write(sep.join(map(str, x)) + end)
n = int(input())
m = int(input())
a = []
b = []
for i in range(n): a.append(input().strip())
for i in range(m): b.append(input().strip())
for x in a:
    for y in b:
        print(x + ' as ' + y)