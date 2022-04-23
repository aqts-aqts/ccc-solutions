from math import sqrt
import sys
input = sys.stdin.readline
n = int(input())
cost = 0
while n > 1:
    factor = 2
    while factor <= sqrt(n) + 1 and n % factor != 0: factor += 1
    if factor < n and n % factor == 0:
        factor2 = n / factor
        n -= factor2
        cost += n / factor2
    else:
        n -= 1
        cost += n
print(int(cost))