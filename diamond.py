#!/usr/bin/python3
count = 3
down_count = 3
down_space = 1
for num1 in range(1, 5):
    for num2 in range(count):
        print("", end=" ")
    count -= 1
    for num3 in range(num1):
        print("*", end=" ")
    print(" ")
for num4 in range(down_count):
    for num5 in range(down_space):
        print("", end=" ")
    down_space += 1
    for num6 in range(down_count):
        print("*", end=" ")
    down_count -= 1
    print(" ")
