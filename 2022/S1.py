n = int(input())
sums = 0
for i in range(0, n, 4):
    if (n - i) % 5 == 0: sums += 1
if n % 4 == 0: sums += 1
print(sums)