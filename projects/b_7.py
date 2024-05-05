"Симметрия в матрицы."

num_n = int(input())
mas = []
for i in range(num_n):
    mas.append(list(map(int, input().split())))
count = 0
for i in range(num_n):
    for num_j in range(num_n):
        if mas[i][num_j] != mas[num_j][i]:
            count += 1

if count > 0:
    print("NO")
else:
    print("YES")
