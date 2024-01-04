""" FOR LOOP IMPLEMENTATION"""

# for num1 in range(10):
#     if num1 == 0 or num1 == 9:
#         for num2 in range(10):
#             print("*", end=" ")
#     else:
#         for num3 in range(10):
#             if num3 == 0 or num3 == 9:
#                 print("*", end=" ")
#             else:
#                 print(" ", end=" ")
#     print(" ")


# for num1 in range(10):
#     for num2 in range(10):
#         if num1 == 0 or num1 == 9:
#             print("*", end=" ")
#         else:
#             if num2 == 0 or num2 == 9:
#                 print("*", end =" ")
#             else:
#                 print(" ", end=" ")
#     print(" ")

""" WHILE LOOP IMPLEMENTATION """

num1 = 0
while num1 < 10:
    num2 = 0
    while num2 < 10:
        if num1 == 0 or num1 == 9:
            print("*", end=" ")
        else:
            if num2 == 0 or num2 == 9:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        num2 += 1
    num1 += 1
    print(" ")

# num1 = 0
# num2 = 0
# num3 = 0
# while num1 < 10:
#     if num1 == 0 or num1 == 9:
#         while num2 < 10:
#             print("*", end=" ")
#             num2 += 1
#     else:
#         while num3 < 10:
#             if num3 == 0 or num3 == 9:
#                 print("*", end=" ")
#             else:
#                 print(",", end=" ")
#             num3 += 1
#     num1 += 1
#     num2 = 0
#     num3 = 0
#     print(" ")
    