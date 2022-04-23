p1=[int(x) for x in input().split()]
p2=[int(x) for x in input().split()]
m = int(input())

dif = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

if m >= dif:
    if dif % 2 == 1 and m % 2 == 1 or dif % 2 == 0 and m % 2 == 0:
        print("Y")
    else:
        print("N")
else:
    print("N")
