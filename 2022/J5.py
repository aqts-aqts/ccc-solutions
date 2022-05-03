import sys
input = sys.stdin.readline

def distanceSort(segment):
    return list(sorted(segment, key=lambda seg: abs(seg[0] - seg[1]), reverse=True))

n = int(input()); t = int(input())
trees = []
for _ in range(t):
    trees.append(tuple(map(int, input().split())))
trees.append((0, 0))
trees.append((n + 1, n + 1))

rowSegments = set(); colSegments = set()
for x, y in trees:
    for nextX, nextY in trees:
        if x != nextX:
            rowSegments.add((min(x, nextX), max(x, nextX)))
        if y != nextY:
            colSegments.add((min(y, nextY), max(y, nextY)))

trees = trees[:-2]
rows = distanceSort(rowSegments)
cols = distanceSort(colSegments)

squares = []
for i in range(2):
    trees = sorted(trees, key=lambda tree: tree[i])
    if i:
        for begin, end in rows:
            nextBegin = 0
            nextEnd = abs(begin - end)
            for tree in trees:
                if begin < tree[0] < end and nextBegin < tree[1] < nextEnd:
                    nextEnd += abs(tree[1] - nextBegin) + 1
                    nextBegin = tree[1] + 1
                if nextEnd > n + 1: break
            else: squares.append(abs(begin - end) - 1)
    else:
        for begin, end in cols:
            nextBegin = 0
            nextEnd = abs(begin - end)
            for tree in trees:
                if begin < tree[1] < end and nextBegin < tree[0] < nextEnd:
                    nextEnd += abs(tree[0] - nextBegin) + 1
                    nextBegin = tree[0] + 1
                if nextEnd > n + 1: break
            else: squares.append(abs(begin - end) - 1)
print(max(squares))