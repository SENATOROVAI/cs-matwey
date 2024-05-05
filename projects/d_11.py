"""Строки в книге."""

num_k: int = int(input())
num_n: int = int(input())
num_a = (num_n - 1) // num_k + 1
num_b = (num_n - 1) % num_k + 1
print(num_a, num_b)
