import collections
n = int(input())
d = {}
for i in range(n):
    b = [int(x) for x in input().split()]
    temp = {b[0]:b[1]}
    d.update(temp)

d = collections.OrderedDict(sorted(d.items()))
keys = list(d.keys())
values = list(d.values())

highest = 0
for k in range(len(keys)-1):
    currentSpeed = abs(values[k+1] - values[k])
    currentTime = abs(keys[k+1] - keys[k])
    MetersPerSecond = currentSpeed / currentTime
    if MetersPerSecond > highest:
        highest = MetersPerSecond


print("%.1f" % highest)