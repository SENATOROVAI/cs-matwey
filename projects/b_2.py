"""Вычисления сколько раз число больше придыдущего."""

num_n: int = int(input())
mass = list(map(int, input().split()))
count = 0
num_b = 1
while num_b < num_n:
    num_a = num_b - 1
    if mass[num_b] > mass[num_a]:
        count += 1
    num_b += 1
print(count)
