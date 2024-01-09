#!/usr/bin/python3
start = 1
space = 0
lower_space = 2
lower_start = 3
for num1 in range(1, 5):
    for num2 in range(space):
        print("", end=" ")
    space += 1
    for num3 in range(start, 5):
        print(num3, end=" ")
    start += 1
    print(" ")
for num4 in range(1, 4):
    for num5 in range(lower_space):
        print("", end=" ")
    lower_space -= 1
    for num3 in range(lower_start, 5):
        print(num3, end=" ")
    lower_start -= 1
    print(" ")
    