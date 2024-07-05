for i in  range (15):
    for j in range (60):
        if i in {0,1,2,3,4,5} and j in {0}:
            print("*", end="")
        elif i in {0,5} and j in {1,2,3,4,5,6,7,8,9}:
            print("*",end="")
        elif i in {4,3,2} and j in {9}:
            print("*",end="")
        elif i in {2} and j in {5,6,7,8}:
            print("*",end="")
        elif i in {0,1,2,3,4,5} and j in {13}:
            print("*",end="")
        elif i in {0,1,2,3,4,5} and j in {17}:
            print("*",end=" ")
        elif i in {0} and j in {18,19,20,21,22,23}:
            print("*",end="")
        elif i in {1,2} and j in {23}:
            print("*",end="")
        elif i in {2} and j in {18,19,20,21,22}:
            print("*",end="")
        elif i in {3} and j in {18}:
            print("*",end="")
        elif i in {4} and j in {20}:
            print("*",end="")
        elif i in {5} and j in {22}:
            print("*",end="")
        elif i in {0,1,2,3,4,5} and j in {28}:
            print("*",end="")
        else:
            print(" ",end="")
    print()