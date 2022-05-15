from math import floor
a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = int(input())

n = (a - b) * floor(s / (a + b))
if s - (a + b) * floor(s / (a + b)) >= a: n += a
elif s - (a + b) * floor(s / (a + b)) < a: n += s - (a + b) * floor(s / (a + b))
if s - (a + b) * floor(s / (a + b)) - a > 0: n -= s - (a + b) * floor(s / (a + b)) - a

y = (c - d) * floor(s / (c + d))
if s - (c + d) * floor(s / (c + d)) >= c: y += c
elif s - (c + d) * floor(s / (c + d)) < c: y += s - (c + d) * floor(s / (c + d))
if s - (c + d) * floor(s / (c + d)) - c > 0: y -= s - (c + d) * floor(s / (c + d)) - c

if n > y: print('Nikky')
elif y > n: print('Byron')
else: print('Tied')