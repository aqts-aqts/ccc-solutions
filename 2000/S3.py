n = int(input())
current = input()
graph = dict()
graph[current] = []

def BFS(source, target):
    visited = dict()
    queue = []

    queue.append(source)
    visited[source] = True
    while queue:
        front = queue.pop(0)
        if front == target:
            return "Can surf from " + source + " to " + target + "."

        for site in graph[front]:
            if not site in visited:
                queue.append(site)
                visited[site] = True
    return "Can't surf from " + source + " to " + target + "."

link = "<A HREF"
end = "</HTML>"
while (n > 0):
    inStream = input()
    while link in inStream:
        if link in inStream:
            left = inStream.index('"')
            inStream = inStream[:left] + '' + inStream[left + 1:]
            right = inStream.index('"')
            inStream = inStream[:right] + '' + inStream[right + 1:]

            graph[current].append(inStream[left:right])
            inStream = inStream.replace(link, '', 1)

    if inStream == end:
        n -= 1
        if (n > 0):
            current = input()
            graph[current] = []

for site in graph:
    for link in graph[site]:
        print("Link from " + site + " to " + link)

site1 = input()
site2 = input()
while site1 != "The End":
    print(BFS(site1, site2))
    site1 = input()
    if site1 != "The End":
        site2 = input()
    else:
        break