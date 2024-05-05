"""Пробежка за день."""

number_x: float = float(input())
number_y: float = float(input())
number_i = number_x
otwet = 1
while number_i < number_y:
    number_i = number_i / 100 * 70 + number_i
    otwet = otwet + 1
print(otwet)
