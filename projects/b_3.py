"""Четные индексы."""

num_n: int = int(input())
mass = list(map(int, input().split()))
print(*mass[::2])
