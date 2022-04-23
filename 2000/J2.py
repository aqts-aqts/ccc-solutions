import sys
input = sys.stdin.readline

def format(str):
    if list(str).count('2') > 0 or list(str).count('3') > 0  or list(str).count('4') > 0  or list(str).count('5') > 0  or list(str).count('7') > 0: return 'no'
    str = str.replace('6', '!')
    str = str.replace('9', '6')
    str = str.replace('!', '9')
    return str

m = int(input())
n = int(input())
count = 0
for i in range(m, n + 1):
    if format(str(i)[::-1]) == str(i):
        count += 1
print(count)