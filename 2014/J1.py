angle1 = int(input())
angle2 = int(input())
angle3 = int(input())

if angle1 == 60 and angle1==angle2==angle3:
    print("Equilateral")
elif angle1 + angle2+angle3==180 and angle1 != angle2 and angle2 != angle3 and angle3 != angle1:
    print("Scalene")
elif angle1+angle2+angle3==180 and angle1 ==angle2 or angle2==angle3 or angle3==angle1:
    print("Isosceles")
else:
    print("Error")