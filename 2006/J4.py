const = [[1,7],[1,4],[2,1],[3,4],[3,5]]
pending = [1,2,3,4,5,6,7]
completed = []
add = []
a = ""
while a != 0:
    a = int(input())
    if a != 0:
        add.append(a)

temp = []
for x in range(len(add)):
    temp.append(add[x])
    
    if len(temp) == 2:
        const.append(temp)
        temp = []

queue = []
unavailable = False
while len(completed) < 7:
    for y in range(len(pending)):
        for z in range(len(const)):
            if pending[y] == const[z][1] and not(const[z][0] in completed):
                unavailable = True
                break

        if unavailable == False:
            queue.append(pending[y])
        unavailable = False

    if len(queue) == 0:
        break

    completed.append(min(queue))
    pending.remove(min(queue))
    
    queue = []

if len(completed) == 7:
    for c in completed:
        print(c, end=" ")
else:
    print("Cannot complete these tasks. Going to bed.")