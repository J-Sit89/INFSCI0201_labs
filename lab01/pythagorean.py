import math

a = float(input("Side A: "))
b = float(input("Side B: "))
c = math.sqrt(a ** 2 + b ** 2)
c_round = round(c, 2)

print("The hypotenuse (C) is : ", c_round)
