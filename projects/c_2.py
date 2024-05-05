"""Угол часовой стрелки."""

num_h: int = int(input())
num_m: int = int(input())
num_s: int = int(input())

print(num_h * 360 / 12 + num_m * 360 / 12 / 60 + num_s * 360 / 12 / 60 / 60)
