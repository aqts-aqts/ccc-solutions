term1 = int(input())
term2 = int(input())

dif = term1 - term2
length = 2
while dif >= 0:
    term1 = term2
    term2 = dif
    dif = term1 - term2
    length += 1
print(length)