f1 = int(input())
f2 = int(input())

def findDiv(num):
    divs = []
    for i in range(1, num + 1):
        if num % i == 0:
            divs.append(i)
    return divs

extras = 0
while f1 >= f2:
    f1 -= f2
    extras += 1

if f1 != 0:
    d1 = findDiv(f1)
    d2 = findDiv(f2)

    cd = []
    for d in d1:
        if d in d2:
           cd.append(d)

    f1 = f1 / cd[len(cd)-1]
    f2 = f2 / cd[len(cd)-1]

if extras != 0:
    print(extras, end=' ')
if f1 != 0:
    print(str(int(f1)) + '/' + str(int(f2)))
else:
    print('0')