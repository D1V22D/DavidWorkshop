import json
book = {}
inner_book ={"name":"","age":0,"phone-no":""}
size = int(input("ENTER THE SIZE =\t"))
for i in range(size):
    names = input("ENTER THE NAME =")
    a = int(input("ENTER THE AGE ="))
    ph_no = input("ENTER THE PHONE NUMBER =")
    inner_book["name"]=names
    inner_book["age"]=a
    inner_book["phone-no"]=ph_no
    book[names]=inner_book
print(book)

s = json.dumps(book)
with open ("D:\\WORKSPACE\\PYTHON\\practice_python\\filejson.json","a") as file :
    file.write(s)
print(file.closed)

# with open ("D:\\WORKSPACE\\PYTHON\\practice_python\\filejson.json","r") as reads:
#     sk = reads.read()

# el = json.loads(sk)
# for person in el:
#     print(el[person])