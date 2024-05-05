"""Символ или цифра."""

num_a: str = input()
num_i: int = ord(num_a)
if 48 <= num_i <= 57:
    print("yes.")
else:
    print("no.")
