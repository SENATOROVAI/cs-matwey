"Обратный порядок."

num_n = int(input())
count = num_n - 1
num_a = [int(value) for value in input().split()]
for i in range(num_n):
    print(num_a[count], end=" ")
    count -= 1
