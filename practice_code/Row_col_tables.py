def assign():
    i = int(input("ENTER THE START UP ="))
    j = int(input("ENTER THE LINE UP ="))
    k = int(input("ENTER THE TIMES YOU WANT ?="))
    print(f"\n\t\tTABLE ({i} - {j})")
    creater(i,j,k)
    # printer(i,j,k)
    
def creater(i,j,k):
    si,le,ti = i,j+1,k+1
    for p in range(si,le):
        for o in range(1,ti):
            g = f"{p}*{o}={p*o}"
            # printer(g)
            print(g)
        print()

# def printer(g,i,j,k):
#     si,le,ti,s = i,j,k,g
#     for v in range(0,ti):
#         for x in range(0,le):
#             print(g)            
assign()