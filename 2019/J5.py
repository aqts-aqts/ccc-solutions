inital = []
replacement = []

for i in range(3):
    x = input().split()
    inital.append(x[0])
    replacement.append(x[1])

s, src, dest = input().split()
s = int(s)

visited = [set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()]

def findChildren(string, s, cur):
    children = []
    for i in range(len(string)):
        pos = i
        passes = 0
        while passes < len(s) and pos < len(string) and string[pos] == s[passes]:
            pos += 1
            passes += 1
        if passes == len(s):
            new = string[:i] + replacement[cur] + string[pos:]
            children.append([cur + 1, i + 1, new])
    return children

def DFS(string, step, graph):
    if step > s:
        return False
    if step == s:
        if string == dest:
            for node in graph:
                print(str(node[0]) + ' ' + str(node[1]) + ' ' + str(node[2]))
            return True
        return False
    if string in visited[step]:
        return False
    for i in range(3):
        children = findChildren(string, inital[i], i)
        for child in children:
            newGraph = graph.copy()
            newGraph.append(child)
            if DFS(child[2], step + 1, newGraph):
                return True
            else:
                visited[step + 1].add(child[2])
    return False

DFS(src, 0, [])