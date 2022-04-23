import math
sequences = [34,71,83,95,107,119,130,142,154,166,178,201,213,225,237,260,272,284,296,331,343,355,390,402,414,461,473,520,532,591,671]
n = int(input())
count=0

if n > 720:
    count += 31 * (math.floor(n / 720))
    n = n % 720

for s in sequences:
    if s <= n:
        count+=1
print(count)