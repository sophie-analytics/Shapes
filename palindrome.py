#!/usr/bin/python3
stop = 2
space = 3
for num1 in range(1, 5):
    for num2 in range(space):
        print(" ", end=" ")
    space -= 1
    for num3 in range(num1):
        print(num1 - num3, end=" ")
    for num4 in range(2, stop):
        if num1 == 1:
            print("")
        else:
            print(num4, end=" ")
    stop += 1
    print(" ")
