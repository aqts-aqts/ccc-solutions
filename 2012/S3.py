n = int(input())
sensors = []
frequencies = []

for i in range(n):
    num = int(input())
    if num not in sensors:
        sensors.append(num)
        frequencies.append(1)
    else:
        frequencies[sensors.index(num)] += 1

biggest = max(frequencies)
top = []
for f in range(len(frequencies)):
    if frequencies[f] == biggest:
        top.append(sensors[f])

out = 0
second = []
if len(top) > 2:
    top.sort()
    print(top[-1] - top[0])
elif len(top) == 2:
    print(abs(top[0] - top[1]))
else:
    sensors.pop(frequencies.index(biggest))
    frequencies.remove(biggest)
    biggest = max(frequencies)
    for f in range(len(frequencies)):
        if frequencies[f] == biggest:
            second.append(sensors[f])
    second.sort()
    if abs(second[0] - top[0]) > abs(second[len(second) - 1] - top[0]):
        print(abs(second[0] - top[0]))
    else:
        print(abs(second[len(second) - 1] - top[0]))
