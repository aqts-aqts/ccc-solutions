n = int(input())
friends = []

def binary_search(left, right):
    while left <= right:
        mid = (right + left) // 2
        score = getSum(mid)
        left_score = getSum(mid - 1)
        right_score = getSum(mid + 1)
        if score < right_score and score < left_score:
            break
        if score == right_score and score == left_score:
            break
        if score < right_score:
            right = mid - 1
        elif score < left_score:
            left = mid + 1
    return score

class friend:
    def __init__(self, pos, speed, dist):
        self.pos = pos
        self.speed = speed
        self.dist = dist
    def findTime(self, c):
        if self.pos <= c + self.dist and self.pos >= c - self.dist:
            return 0
        else:
            if self.pos > c:
                return abs(self.pos - (c + self.dist)) * self.speed
            else:
                return abs(self.pos - (c - self.dist)) * self.speed

def getSum(c):
    dist = 0
    for f in friends:
        walk = abs(c - f.pos) - f.dist
        if walk > 0:
            dist += walk * f.speed
    return dist

left = 2147483647
right = 0

for i in range(n):
    temp = input().split()
    friends.append(friend(int(temp[0]), int(temp[1]), int(temp[2])))
    if friends[i].pos > right:
        right = friends[i].pos
    if friends[i].pos < left:
        left = friends[i].pos

print(binary_search(left, right))