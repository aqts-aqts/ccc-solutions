import sys
input = sys.stdin.readline
print = lambda *x, sep=' ', end='\n': sys.stdout.write(sep.join(map(str, x)) + end)

def factors(n):
    f = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0: f.add(i); f.add(n // i)
    return f

n = int(input())
m = int(input())
count = 0
for i in range(n, m + 1):
    if len(factors(i)) == 4: count += 1
print('The number of RSA numbers between ' + str(n) + ' and ' + str(m) + ' is ' + str(count))