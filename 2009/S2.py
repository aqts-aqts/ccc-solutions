# The largest test case has only 26 possible light patterns, can we make an observation here?

r = int(input())
l = int(input())

lights = [int(''.join(input().split()), 2) for _ in range(r)]
states = [set() for _ in range(r)]

states[0].add(lights[0])
for i in range(1, r):
    states[i].add(lights[i])
    for state in states[i - 1]:
        states[i].add(state ^ lights[i])

print(len(states[-1]))