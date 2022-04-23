n = int(input())
d = 1
a = 1
for i in range(n):
    print('*' * a,end='')
    print(' ' * (2 * n - 2 * a),end='')
    print('*' * a)
    a += d * 2
    if 2 * n - 2 * a == 0:
        d = -1