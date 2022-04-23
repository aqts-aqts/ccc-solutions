n = int(input())
friends = [[],[],[],[],[],[],[]]
fset = [i + 1 for i in range(n - 1)]

def findAllNodes(source):
    visited = [False] * 7
    queue = []
    nodes = []

    queue.append(source)
    visited[source] = True
    while queue:
        front = queue.pop(0)

        for f in friends[front]:
            if visited[f] == False:
                nodes.append(f)
                queue.append(f)
                visited[f] = True
    return nodes

def powerset(x):
    m = []
    if not x:
        m.append(x)
    else:
        A = x[0]
        B = x[1:]
        for z in powerset(B):
            m.append(z)
            r = [A] + z
            m.append(r)
    return m

for i in range(n - 1):
    friends[int(input())].append(i + 1)

valid = []
for s in powerset(fset):
    v = True
    for x in s:
        nodes = findAllNodes(x)
        if set(nodes).issubset(s):
            continue
        else:
            v = False
            break
    if v:
        valid.append(s)

print(len(valid))