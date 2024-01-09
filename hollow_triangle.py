#!/usr/bin/python3
count = 4
for num1 in range(1, 6):
    for num2 in range(count):
        print("", end=" ")
    count -= 1
    for num3 in range(num1):
        if num1 == 1 or num1 == 5:
            print("*", end=" ")
        else:
            if num3 == 0 or num3 == num1 - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
    print(" ")
