length = int(input()); height = int(input()); cornerLength = int(input()); cornerHeight = int(input())
steps = int(input())
room = []

for _ in range(cornerHeight): # Initalize matrix
    room.append([True if i < cornerLength or i >= length - cornerLength else False for i in range(length)])
for _ in range(height - cornerHeight * 2):
    room.append([False] * length)
for _ in range(cornerHeight):
    room.append([True if i < cornerLength or i >= length - cornerLength else False for i in range(length)])

position = [0, cornerLength]
priority = True # True = right priority, False = left priority
while steps > 0:
    moved = False # Check if trapped
    room[position[0]][position[1]] = True
    if priority:
        try: # Right
            if not room[position[0]][position[1] + 1]:
                moved = True
                position[1] += 1
                steps -= 1
                continue
        except: pass
        try: # Down
            if not room[position[0] + 1][position[1]]:
                moved = True
                position[0] += 1
                steps -= 1
                continue
        except: pass
        try: # Left
            if not room[position[0]][position[1] - 1]:
                moved = True
                position[1] -= 1
                steps -= 1
                continue
        except: pass
        try: # Up
            if not room[position[0] - 1][position[1]]:
                moved = True
                priority = False # Switch to left priority
                position[0] -= 1
                steps -= 1
                continue
        except: pass
    else:
        try: # Left
            if not room[position[0]][position[1] - 1]:
                moved = True
                position[1] -= 1
                steps -= 1
                continue
        except: pass
        try: # Up
            if not room[position[0] - 1][position[1]]:
                moved = True
                position[0] -= 1
                steps -= 1
                continue
        except: pass
        try: # Right
            if not room[position[0]][position[1] + 1]:
                moved = True
                position[1] += 1
                steps -= 1
                continue
        except: pass
        try: # Down
            if not room[position[0] + 1][position[1]]:
                moved = True
                priority = True # Switch to right priority
                position[0] += 1
                steps -= 1
                continue
        except: pass
    if not moved: # Exit if trapped
        break
print(position[1] + 1)
print(position[0] + 1)