#!/usr/bin/python3
count = 3
down_count = 3
down_space = 1
for num1 in range(1, 5):
    for num2 in range(count):
        print("", end=" ")
    count -= 1
    for num3 in range(num1):
        if num1 == 1:
            print("*", end=" ")
        else:
            if num3 == 0 or num3 == num1 - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
    print(" ")
for num4 in range(down_count):
    for num5 in range(down_space):
        print("", end=" ")
    down_space += 1
    for num6 in range(down_count):
        if num4 == 4:
            print("*", end=" ")
        else:
            if num6 == 0 or num6 == down_count - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
    down_count -= 1
    print(" ")