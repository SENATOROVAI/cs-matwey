"""The rook's move."""

x_1 = int(input())
y_1 = int(input())
x_2 = int(input())
y_2 = int(input())

if x_1 == x_2 or y_2 == y_1:
    print("YES")
else:
    print("NO")
