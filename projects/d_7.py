"""Электронные часы."""

num_m: int = int(input())
num_a: int = num_m % (60 * 24) // 60
num_b: int = num_m % 60
print(num_a, num_b)
