import sys
input = sys.stdin.readline

humidity = int(input())
maxHours = int(input())

altitude = sys.maxsize
hour = 0
while altitude > 0 and hour < maxHours:
    hour += 1
    altitude = -6 * hour ** 4 + humidity * hour ** 3 + 2 * hour ** 2 + hour
if altitude > 0: print('The balloon does not touch ground in the given time.')
else: print('The balloon first touches ground at hour: \n' + str(hour))