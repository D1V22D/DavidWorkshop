class Var_Use :
    l = 25 # class variable 
    def __init__(self): # constructor 
        self.a=10 # instance variable
        self.aa=20
        print("{dcls}enter",format (self.a + self.aa))
    @classmethod # class method decorator
    def name (cls): # called by class with decorator
        print("k means")
    def  pilli (cls): # called by class with class and pass class as argument 
        print("k meanscls of")
na = Var_Use()
Var_Use.pilli(Var_Use)
Var_Use.name()   