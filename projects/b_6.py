"Максимум в массиве."

num_n = int(input())
count = num_n - 1
otwet = 0
num_a = [int(value) for value in input().split()]
for i in range(num_n):
    for num_e in range(num_n - 1):
        if num_a[i] <= num_a[num_e]:
            num_a[i] = num_a[num_e]
print(num_a[i])
