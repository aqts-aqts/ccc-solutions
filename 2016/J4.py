import math
def convertMinutes(th, h, tm, m):
    mins = 0
    mins += th * 600
    mins += h * 60
    mins += tm * 10
    mins += m
    return mins

def convertTime(mins):
    mins = int(mins)
    th = math.floor(mins / 600)
    h = math.floor((mins-th*600) / 60)
    
    if th >= 2 and h >= 4:
        th -= 2
        h -= 4

    if len(str(mins % 60)) == 1:
        time = str(th) + str(h) + ':0' + str(mins % 60)
    else:
        time = str(th) + str(h) + ':' + str(mins % 60)
    return time

t = input()
th = int(t[0])
h = int(t[1])
tm = int(t[3])
m = int(t[4])

mins = convertMinutes(th, h, tm, m)
o = mins + 120
passed = 0
mm = mins
while mm < o:
    if mins + passed >= 420 and mins + passed < 600 or mins + passed >= 900 and mins + passed < 1140:
        passed+=1
        mm+=0.5
    else:
        passed+=1
        mm+=1
print(convertTime(mins + passed))