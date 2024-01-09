#!/usr/bin/python3
space = 0
space_down = 3
count = 4
for num1 in range(1, 5):
    for num2 in range(space):
        print("", end=" ")
    space += 1
    for num3 in range(count):
        if num1 == 1 or num1 == 4:
            print("*", end=" ")
        else:
            if num3 == 0 or num3 == count - 1 :
                print("*", end=" ")
            else:
                print(" ", end=" ")
    count -= 1
    print(" ")
for num4 in range(1, 5):
    for num5 in range(space_down):
        print("", end=" ")
    space_down -= 1
    for num6 in range(num4):
        if num4 == 1 or num4 == 4:
            print("*", end=" ")
        else:
            if num6 == 0 or num6 == num4 - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
    print(" ")
