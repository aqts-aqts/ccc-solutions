x = int(input()); m = int(input())
b=False
for i in range(m):
    if (x * i) % m == 1:
        print(i)
        b=True
        break
if not b:
    print('No such integer exists.')