size = int(input("ENTER THE RANGE ="))
i = 0
def fibanocci():
    a,b = 0,1
    while True:
        yield a # the yield is a generator used as a return statement and invoked by the next method in iterator
        a,b = b,a+b


for i in fibanocci():
    i += 1
    if i > size:
        break
    print(i,end="..")
print("\nend =",i)