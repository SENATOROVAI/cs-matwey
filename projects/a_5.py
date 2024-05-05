"""Палендром без пробелов."""

num_a: str = input()
num_c: int = 1
otwet: int = 1
for i in range(len(num_a)):
    if num_a[i] != num_a[-num_c]:
        otwet = otwet - 1
        num_c = num_c + 1
    else:
        num_c = num_c + 1
if otwet == 1:
    print("yes")
else:
    print("no")
