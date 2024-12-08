import sys
input = sys.stdin.readline

string = input().strip()
x = int(input())

class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.nutrients = [0] * (x + 1)
class Leaf:
    def __init__(self, value):
        self.value = value
        self.nutrients = [0] * (x + 1)

def createNode(s):
    if not s.startswith('('):
        return Leaf(int(s))
    else:
        s = s[1:len(s) - 1].strip()
        i = 0
        if s.startswith('('):
            count = 1
            i = 1
            while count > 0:
                if s[i] == '(':
                    count += 1
                elif s[i] == ')':
                    count -= 1
                i += 1
        else:
            i = s.index(' ')
        return Node(createNode(s[:i]), createNode(s[i + 1:]))

def solve(node, x):
    if isinstance(node, Leaf): # leaf node
        for i in range(x + 1):
            node.nutrients[i] = node.value + i # fill up nutrients[]
    else:
        solve(node.left, x) # fill up left subtree
        left = [0] * (x + 1) # max of left subtree using i agents
        for i in range(x + 1): # checking max from agents to branches
            maxLeft = 0
            for j in range(i + 1):
                maxLeft = max(maxLeft, min((1 + j) ** 2, node.left.nutrients[i - j])) # used j agents on branches, so i - j left on leaves
            left[i] = maxLeft

        solve(node.right, x) # fill up right subtree
        right = [0] * (x + 1) # max of right subtree using i agents
        for i in range(x + 1): # checking max from agents to branches
            maxRight = 0
            for j in range(i + 1):
                maxRight = max(maxRight, min((1 + j) ** 2, node.right.nutrients[i - j])) # used j agents on branches, so i - j left on leaves
            right[i] = maxRight
        
        for i in range(x + 1): # combining left and right subtrees
            maxCombined = 0
            for j in range(i + 1):
                maxCombined = max(maxCombined, left[j] + right[i - j]) # used j agents on left subtree, so i - j left on right
            node.nutrients[i] = maxCombined

root = createNode(string)
solve(root, x)
print(root.nutrients[x])