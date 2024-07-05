r = int(input("ENTER THE NUMBER OF  TIMES=\t"))
c = int(input("ENTER THE NUMBER OF TABLES=\t"))
for i in range(1,r+1):
    for j in range(1,c+1):
        print("{:2d} * {:2d} =".format(i,j),"{:2d}".format(i*j),end=' ')
    print()
