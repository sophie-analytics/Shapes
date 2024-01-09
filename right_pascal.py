#!/usr/bin/python3
for num1 in range(1,8):
    if num1 % 2 != 0:
        print("*", end=" ")
    else:
        print(" ", end=" ")
    for num3 in range(2, 5):
        if (num1 / num3) == 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print(" ")
