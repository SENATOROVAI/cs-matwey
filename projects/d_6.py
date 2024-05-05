"""Сумма цифр."""

num_aa: int = int(input())
num_a: int = num_aa // 100
num_b: int = (num_aa // 10) % 10
num_c: int = num_aa % 10
num_bb: int = num_a + num_b + num_c
print(num_bb)
