i = float(input())
j = float(input())

bmi = i/(j*j)
if bmi > 25:
    print("Overweight")
elif bmi <= 25 and bmi >= 18.5:
    print("Normal weight")
else:
    print("Underweight")
