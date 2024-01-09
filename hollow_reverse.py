#!/usr/bin/python3
down_space = 1
down_count = 5
for num1 in range(down_count):
    for num2 in range(down_space):
        print("", end=" ")
    down_space += 1
    for num3 in range(down_count):
        if num1 == 0 or num1 == 4:
            print("*", end=" ")
        else:
            if num3 == 0 or num3 == down_count - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
    down_count -= 1
    print(" ")
