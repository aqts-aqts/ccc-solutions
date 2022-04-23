burgers = [0, 461, 431, 420, 0]
drinks = [0, 130, 160, 118, 0]
sides = [0, 100, 57, 70, 0]
desserts = [0,167,266,75,0]

b=int(input())
d=int(input())
s=int(input())
dess=int(input())
print("Your total Calorie count is " + str(burgers[b]+sides[d]+drinks[s]+desserts[dess]) + ".")
