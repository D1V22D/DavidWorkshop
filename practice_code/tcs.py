natural = []
num = int(input("Enter the number of list in natural numbers =\t"))
c =0
while num-1 >= c :
    if c >= 0:
        it = int(input("Enter the list items =\t"))
        if it > 0 and it < 11:
            natural.append(it)
            c+=1
        else:
            c-=1
    else:
        c = 0
natural.sort()
mi =min(natural)
natural.remove(mi)
print(mi)
print(natural)
  