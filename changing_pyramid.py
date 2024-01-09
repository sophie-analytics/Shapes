#!/usr/bin/python3
increment = 0
start = 1
for num1 in range(1, 5):
    index = 0
    for num2 in range(start, 11):
        if index >= num1:
            break
        else:
            print(num2, end=" ")
        index += 1
    increment += 1
    start += increment
    print(" ")
