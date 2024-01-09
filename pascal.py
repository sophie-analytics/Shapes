#!/usr/bin/python3
# space = 3
# for num1 in range(1, 5):
#     no = [1]
#     for num2 in range(space):
#         print("", end=" ")
#     space -= 1
#     for num3 in range(num1):
#         if num1 == 1:
#             print(no[num3], end=" ")
#         else:
#             for num4 in range(1, num1):
#                 no.append(no[num3] + 1)
#             print(no[num3], end=" ")
#     print(" ")

space = 3
result = [1]
for num1 in range(1, 5):
    for num2 in range(space):
        print("", end=" ")
    space-= 1
    for num3 in range(num1):
      