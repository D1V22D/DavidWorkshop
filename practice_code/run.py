# import Write_format as wf
import time

i1 = [1, 2, 3]
i2 = [4, 5, 6]
i3 = [7, 8, 9]
i4 = [10, 11, 12]
i5 = [13, 14, 15]
char = "*"


def writeRun():
    i = 0
    while True:
        j = 0
        while True:
            i+=1
            if i == 0 and j in set(i1):
                print("{:2s}".format(char), end="")
            elif i == 1 and j in set(i2):
                print("{:2s}".format(char), end="")
            elif i == 2 and j in set(i3):
                print("{:2s}".format(char), end="")
            elif i == 3 and j in set(i4):
                print("{:2s}".format(char), end="")
            elif i == 4 and j in set(i5):
                print("{:2s}".format(char), end="")
            else:
                print("{:2s}".format(" "), end="")
            print()
        print()
        time.sleep(0.5)


writeRun()
