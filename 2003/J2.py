import sys
sys.setrecursionlimit(int(1e9))
input = sys.stdin.readline
print = lambda *x, sep=' ', end='\n': sys.stdout.write(sep.join(map(str, x)) + end)
c = int(input())
while c != 0:
    p = sys.maxsize
    x = sys.maxsize
    y = sys.maxsize
    for i in range(1, int(c ** 0.5) + 1):
        if c % i == 0: 
            if i * 2 + (c // i) * 2 < p: p = i * 2 + (c // i) * 2; x = i; y = c // i
    print('Minimum perimeter is ' + str(p) + ' with dimensions ' + str(x) + ' x ' + str(y))
    c = int(input())