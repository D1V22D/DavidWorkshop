li = ["Friend","Love","Affection","Marriage","Enemy","Sibling"]

def wordcount():
    name1 = input("Enter name 1 =\t")
    name2 = input("Enter name 2 =\t")
    for i in name1:
        for j in name2:
            if i==j:
                name1 = name1.replace(i,'',1)
                name2 = name2.replace(i,'',1)
                break
            else:
                continue 
    count = len(name1)+len(name2)
    print(check_relation(count))

def check_relation(count):
    c = count
    while len(li) > 1:
        if len(li)-1 < c-1:
            c = abs((len(li)) - (count))-1
        else:
            del li[c]
            continue
    return li

wordcount()