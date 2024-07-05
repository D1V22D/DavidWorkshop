# import time
# i = -1
# j = 0
# k = [4]

# while i < 4:
#     i +=1
#     while j>=0:
#         if i == 0 and j in set(k):
#             print("{:2s}".format("*"), end="")
#         elif i == 1 and j in {3}:
#             print("{:2s}".format("*"), end="")
#         elif i == 2 and j in {2}:
#             print("{:2s}".format("*"), end="")
#         elif i == 3 and j in {1}:
#             print("{:2s}".format("*"), end="")
#         elif i == 4 and j in {0}:
#             print("{:2s}".format("*"), end="")
#         else:
#             print("{:2s}".format(" "), end="")
#         time.sleep(0.5)
#         j +=1
#         k.append(j)
#     print()
# print()
import time

name_pattern = [
    "****   *  *  ****",
    "*   * * *  *    *",
    "*   * **    ****",
    "*   * * *      *",
    "**** *  * ****",
]

while True:
    for i in range(20):
        print("\r", end="")
        for line in name_pattern:
            print(" " * i + line, end="")
        time.sleep(0.1)

    for i in range(18, 0, -1):
        print("\r", end="")
        for line in name_pattern:
            print(" " * i + line, end="")
        time.sleep(0.1)
