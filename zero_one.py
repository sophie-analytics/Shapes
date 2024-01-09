#!/usr/bin/python3
count = [1, 0]
for num1 in range(1, 5):
    index = 0
    for num2 in range(1, num1 + 1):
        for num3 in count:
            if index >= num1:
                break
            else:
                print(num3, end=" ")
            index += 1
    print(" ")
