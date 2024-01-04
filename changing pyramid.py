#!/usr/bin/python3
increment1 = 0
increment2 = 2
for num1 in range(1, 5):
    if num1 == 1:
        print(num1, end=" ")
    else:
        for num2 in range(num1 + increment1, num1 + increment2):
            print(num2, end=" ")
    increment1 += 1
    increment2 += 3
    print(" ")
