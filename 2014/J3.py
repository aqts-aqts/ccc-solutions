toDo = int(input())
totals = []
for d in range(toDo):
    nums = input().split()
    for n in range(len(nums)):
        nums[n] = int(nums[n])
    totals.append(nums)

apts = 100
dpts = 100
for v in totals:
    if v[0] < v[1]:
        apts -= v[1]
    elif v[1] < v[0]:
        dpts -= v[0]

print(apts)
print(dpts)