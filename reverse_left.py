#!/usr/bin/python3
count = 5
for num1 in range(count):
    for num2 in range(num1):
        print(" ", end=" ")
    for num3 in range(count):
        print("*", end=" ")
    count -= 1
    print(" ")