"""Стоимость булочек."""

num_a: int = int(input())
num_b: int = int(input())
num_k: int = int(input())
num_c: int = num_k * (100 * num_a + num_b)
print(num_c // 100, num_c % 100)
