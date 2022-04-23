import sys
input = sys.stdin.readline

day, days = map(int, input().split())
print('Sun Mon Tue Wed Thr Fri Sat')
currentline = ' ' * (4 * (day - 1))
c = 1
d = day - 1
while c <= days:
    if d == 7:
        print(currentline[1:])
        currentline = ''
        d = 0
    currentline += ' ' * (4 - len(str(c)))
    currentline += str(c)
    c += 1
    d += 1
print(currentline[1:])