n = int(input())

def rotate(arr):
    for x in range(0, int(n / 2)):
        for y in range(x, n-x-1):
            temp = arr[x][y]
            arr[x][y] = arr[y][n-1-x]
            arr[y][n-1-x] = arr[n-1-x][n-1-y]
            arr[n-1-x][n-1-y] = arr[n-1-y][x]
            arr[n-1-y][x] = temp
    return arr

def isValid(arr):
    y=[x[0] for x in arr]
    return arr[0] == sorted(arr[0]) and y == sorted(y)

sunflowers = []
for i in range(n):
    sunflowers.append([int(x) for x in input().split()])

while not isValid(sunflowers):
    sunflowers = rotate(sunflowers)

for s in sunflowers:    
    print(' '.join([str(x) for x in s]))
