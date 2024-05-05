"""Четные елементы."""

num_n: int = int(input())
mass = list(map(int, input().split()))
for i in range(num_n):
    if mass[i] % 2 == 0:
        print(mass[i], end=" ")
