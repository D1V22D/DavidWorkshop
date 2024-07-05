# class part_1:
#     def Outer_func():
#         message =" Hi "
        
#         def Inner_func():
#             name = input("give your name ?\n")
#             return f"{message} ! {name}"
#         return Inner_func()

#     print(Outer_func())
name = input("NAME =")
def Outer_func1(mes):  
    def Inner_func1():
        return mes() # if we don`t put round braces then it could n`t define as a function otherwise it can be invoked with the reference varible like object 
    return Inner_func1

def namepass():
    print(name+"! Hi")
# the below sytax similar to the @Outer_func1
namefind = Outer_func1(namepass)# creating like a object to get the reference of the inner function

namefind()