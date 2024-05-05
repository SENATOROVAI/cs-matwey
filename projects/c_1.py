"""Вещественное равенство."""

number_a: float = float(input())
number_b: float = float(input())
number_c: float = float(input())

eps = 1e-8

if abs(number_a + number_b - number_c) < eps:
    print("YES")
else:
    print("NO")
