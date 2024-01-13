#!/usr/bin/python3
max_no = 7
mid_no = max_no // 2
temp = max_no
for num1 in range(max_no):
    temp = temp - 1
    for num2 in range(num1 + 1):
        if num1 <= mid_no:
            if num1 % 2 == 0:
                if num2 % 2 == 0:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            else:
                if num2 % 2 == 1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
        else:
            if num2 <= temp:
                if num1 % 2 != 0:
                    if num2 % 2 != 0:
                        print("*", end=" ")
                    else:
                        print(" ", end=" ")
                else:
                    if num2 % 2 == 0:
                        print("*", end=" ")
                    else:
                        print(" ", end=" ")
    print(" ")
