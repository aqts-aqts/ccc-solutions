from collections import deque
import sys
input = sys.stdin.readline
print = sys.stdout.write

code = ''
line = input()
while '#' not in line:
    code += line; line = ''.join([x if x in '><+-[].#' else '' for x in input()])
code += line.replace('#', '')
code = code.replace('-[[->+<]>-]', '>' * 255)

def findMatching(cc):
    layer = 0
    for i in range(len(cc)):
        if cc[i] == '[': layer += 1
        elif cc[i] == ']': layer -= 1
        if layer == 0: return i

memory = [0]
loop = deque()
cc, c = 0, 0
while cc < len(code):
    command = code[cc]
    if command == '>': 
        c += 1
        if c == len(memory): memory.append(0)
    if command == '<':
        c = 0 if c <= 0 else c - 1

    if command == '+':
        memory[c] = memory[c] + 1 if memory[c] < 255 else 0
    if command == '-':
        memory[c] = memory[c] - 1 if memory[c] > 0 else 255
    
    if command == '[':
        if memory[c] == 0: cc += findMatching(code[cc:])
        else: loop.append(cc)
    if command == ']':
        if memory[c] == 0: loop.pop()
        else: cc = loop[-1]
    
    if command == '.': print(chr(memory[c]))
    cc += 1