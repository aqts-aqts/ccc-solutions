import sys
input = sys.stdin.readline
nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
subs = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
vals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
keys = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

def decimal(num):
    total = 0
    for sub in subs:
        if sub in num:
            total += subs[sub]
            num = num.replace(sub, '')
    for n in nums:
        if n in num:
            total += nums[n] * num.count(n)
            num = num.replace(sub, '')
    return total

def roman(num):
    n = ''
    i = 0
    while num > 0:
        for _ in range(num // vals[i]):
            n += keys[i]
            num -= vals[i]
        i += 1
    return n

for _ in range(int(input())):
    equation = input().strip()
    num1, num2 = equation.split('+')
    num2 = num2.replace('=', '')
    n1 = decimal(num1)
    n2 = decimal(num2)
    if n1 + n2 <= 1000: print(num1 + '+' + num2 + '=' + roman(n1 + n2))
    else: print(num1 + '+' + num2 + '=' + 'CONCORDIA CUM VERITATE')