import sys
input = sys.stdin.readline
def solve(sentence):
    for i in range(len(sentence)):
        if len(sentence[i]) == 4: sentence[i] = '****'
    print(' '.join(sentence))
n = int(input())
for _ in range(n): sentence = input().split(); solve(sentence)
