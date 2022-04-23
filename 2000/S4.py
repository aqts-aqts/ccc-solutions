import sys
sys.setrecursionlimit(1000000000)

dist = int(input())
n = int(input())

clubs = []
for i in range(n):
    clubs.append(int(input()))
 
def ss(r, visited=dict()):
    if r in visited:
        return visited[r]
    if r == 0:
        return []
    elif r < 0:
        return None

    shortest = None
    for c in clubs:
        dif = r - c
        s = ss(dif)
        if s != None:
            combo = s + [c]
            if shortest == None or len(combo) < len(shortest):
                shortest = combo.copy()
    
    visited[r] = shortest
    return shortest

result = ss(dist)
if result != None:
    print("Roberta wins in " + str(len(result)) + " strokes.")
else:
    print("Roberta acknowledges defeat.")