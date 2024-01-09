#!/usr/bin/python3
no = [1, 2, 3, 4]
space = 0
for num1 in range(4):
    fix = no[num1:]
    for num2 in range(space):
        print("", end=" ")
    space += 1
    for index in fix:
        print(index, end=" ")
    fix = []
    print(" ")
