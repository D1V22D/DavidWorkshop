import logging
a = [10,5,6,"hello",0,9,"david",0]
def Exceptionsnew():
    for i in a :
            try :
                print(10 / i)
            except TypeError as e :
                print(f"ERROR :{type(e).__name__}")
            except ZeroDivisionError as e :
                print(f"ERROR :{e}")
            except Exception as e :
                logging.exception(e)

base = float(input("enter the base ="))
power =float(input("enter the power ="))         
def __pow__(base , power):
    c =1
    for i in range(power):
        c = base-c
    return c

print(__pow__(base,power))
    