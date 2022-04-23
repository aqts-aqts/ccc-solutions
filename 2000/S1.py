q = int(input())
m1 = int(input())
m2 = int(input())
m3 = int(input())

p = 0
while True:
    if q > 0:
        m1 += 1
        q -= 1
        p += 1
        if m1 == 35:
            q += 30
            m1 = 0
    else:
        break
    if q > 0:
        m2 += 1
        q -= 1
        p += 1
        if m2 == 100:
            q += 60
            m2 = 0
    else:
        break
    if q > 0:
        m3 += 1
        q -= 1
        p += 1
        if m3 == 10:
            q += 9
            m3 = 0
    else:
        break
print('Martha plays ' + p + ' times before going broke.')