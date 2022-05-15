def formatTime(time):
    minutes = time % 100
    minutes += (time // 100) * 60
    return minutes

def encodeTime(time):
    if time < 0: time += 1440
    elif time >= 1440: time -= 1440
    hours = time // 60
    mins = time % 60
    if mins < 10 and hours > 0: mins = '0' + str(mins)
    if hours > 0: return str(hours) + str(mins)
    else: return str(mins)

time = formatTime(int(input()))
print(encodeTime(time) + ' in Ottawa')
print(encodeTime(time - 180) + ' in Victoria')
print(encodeTime(time - 120) + ' in Edmonton')
print(encodeTime(time - 60) + ' in Winnipeg')
print(encodeTime(time) + ' in Toronto')
print(encodeTime(time + 60) + ' in Halifax')
print(encodeTime(time + 90) + ' in St. John\'s')