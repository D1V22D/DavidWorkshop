s=1
e=int(input("enter the range ="))
a=[]
for i in range(s,e+1):
    b=float(input("Enter the list elements (float)"+str(i)+ " = "))
    a.append(b)
print(a)
x=0
for i in a:
    x=x+i
print("the list sum =",float(x))
