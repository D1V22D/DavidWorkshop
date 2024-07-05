a=[]
def tip():
    for i in range(5):
        b=int(input("Enter the elements of list ="))
        a.append(b)
    print("the list elements: ",a)
def lic(s):
    #print(type(a)) the a is the list data type
    for j in a:#the a is substitute on j to become the int
        #print(type(j))
        s+=j
    print("the sum of list elements: ",s)
tip()
lic(0)


