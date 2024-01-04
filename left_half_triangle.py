count = 4
for num1 in range(1, 6):
    for num2 in range(count):
        print(" ", end=" ")
    count -= 1
    for num3 in range(num1):
        print("*", end=" ")
    print(" ")
