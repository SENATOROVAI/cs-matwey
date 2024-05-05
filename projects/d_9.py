"""Парты."""

n_a: int = int(input())
n_b: int = int(input())
n_c: int = int(input())
n_d: int = n_a // 2 + n_a % 2 + n_b // 2 + n_b % 2 + n_c // 2 + n_c % 2
print(n_d)
