lis_t = ['a','b','c','d','e']
b = 0
while b != 4:
    b = int(input())
    n = int(input())

    for x in range(n):
        if b == 1:
            temp = lis_t.pop(0)
            lis_t.append(temp)
        elif b == 2:
            temp = lis_t.pop(4)
            lis_t.insert(0, temp)
        elif b == 3:
            temp = lis_t.pop(0)
            lis_t.insert(1, temp)
        else:
            for l in lis_t:
                print(str(l.upper()), end=" ")
            break
