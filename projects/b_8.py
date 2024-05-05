"Макимум в матрице."

num_n, num_m = map(int, input().split())
res = -1
for i in range(num_n):
    lst = list(map(int, input().split()))
    for num_j in range(num_m):
        if lst[num_j] > res:
            row, col = i, num_j
            res = lst[num_j]
print(res)
print(row, col)
