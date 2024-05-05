"""Количесвто слов."""

num_a: str = input()
space = 0
for i in range(len(num_a)):
    if ord(num_a[i]) == ord(" "):
        space = space + 1
print(space + 1)
