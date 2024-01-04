#!/usr/bin/python3
for num1 in range(10):
    if num1 == 0 or num1 == 9:
        for num2 in range(10):
            print("*", end=" ")
    else:
        for num3 in range(10):
            if num3 == 0 or num3 == 9:
                print("*", end=" ")
            else:
                print(" ", end=" ")
    print(" ")
