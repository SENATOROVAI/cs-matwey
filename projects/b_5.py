"Циклически вправо."

num_n = int(input())
num_a = [int(value) for value in input().split()]
print(num_a[-1], end=" ")
for i in range(num_n - 1):
    print(num_a[i], end=" ")
