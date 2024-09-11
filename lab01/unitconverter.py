import sys

cm_IN = 1 / 2.54
in_CM = 2.54
yd_M = 0.9144
m_YD = 1 / 0.9144
oz_G = 28.349523125
g_OZ = 1 / 28.349523125
lb_KG = 0.45359237
kg_LB = 1 / 0.45359237

user_input = input("Give me a value WITH the units ")
value_str, unit = user_input.split()

value = float(value_str)

#for the following, used chatGPT to copy one elif into the other ones, like so i wouldnt have to type them out manually

if unit == "cm":
    converted_value = value * cm_IN
    converted_unit = "in"
elif unit == "in":
    converted_value = value * in_CM
    converted_unit = "cm"
elif unit == "yd":
    converted_value = value * yd_M
    converted_unit = "m"
elif unit == "m":
    converted_value = value * m_YD
    converted_unit = "yd"
elif unit == "oz":
    converted_value = value * oz_G
    converted_unit = "g"
elif unit == "g":
    converted_value = value * g_OZ
    converted_unit = "oz"
elif unit == "lb":
    converted_value = value * lb_KG
    converted_unit = "kg"
elif unit == "kg":
    converted_value = value * kg_LB
    converted_unit = "lb"
else:
    print("I don't know what that unit is, sorry dude")
    exit

converted_value_round = round(converted_value, 2)

print(user_input, " is equvalent to ", converted_value_round, converted_unit)
