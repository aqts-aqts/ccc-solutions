from decimal import *
getcontext().prec = 28

n = int(input())

sheep = []
for i in range(n):
    x = Decimal(input())
    y = Decimal(input())
    sheep.append((x, y))

for i in range(n):
    interval = [0, 1000]

    for j in range(n):
        if i == j:
            continue
    
        x1, y1 = sheep[i]
        x2, y2 = sheep[j]

        if x1 == x2:
            if y1 > y2:
                interval = [1, 0]
                break
            continue
        elif x1 > x2:
            min_x = x2 ** 2 / (2 * (-x1 + x2)) + y2 ** 2 / (2 * (-x1 + x2)) - x1 ** 2 / (2 * (-x1 + x2)) - y1 ** 2 / (2 * (-x1 + x2))
            interval[0] = max(interval[0], min_x)
        else:
            max_x = x2 ** 2 / (2 * (-x1 + x2)) + y2 ** 2 / (2 * (-x1 + x2)) - x1 ** 2 / (2 * (-x1 + x2)) - y1 ** 2 / (2 * (-x1 + x2))
            interval[1] = min(interval[1], max_x)
        
        if interval[0] > interval[1]:
            break
    
    if interval[0] <= interval[1]:
        print("The sheep at (" + '{:.2f}'.format(sheep[i][0]) + ", " + '{:.2f}'.format(sheep[i][1]) + ") might be eaten.")