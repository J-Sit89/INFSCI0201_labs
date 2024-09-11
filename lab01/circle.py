import math

radius = float(input ("Gimme dat radius: "))
area = math.pi * radius ** 2
area_round = round(area, 2)
perimeter = 2 *math.pi * radius
perimeter_round = round(perimeter, 2)

print("The circle with radius",radius,"has an area of",area_round, "and a perimeter of",perimeter_round)