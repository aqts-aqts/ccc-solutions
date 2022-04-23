r, c = input().split()
r = int(r)
c = int(c)
k = int(input())

cats = []
for i in range(k):
    cell = [int(x) for x in input().split()]
    cats.append((cell[0], cell[1]))

def findPaths(row, column, visited = dict()):
    if (row, column) in visited:
        return visited[(row, column)]
    if (row, column) in cats or row == 0 or column == 0:
        return 0
    elif row == 1 and column == 1:
        return 1

    visited[(row, column)] = findPaths(row - 1, column) + findPaths(row, column - 1)
    return visited[(row, column)]

print(findPaths(r, c))