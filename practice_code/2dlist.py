class TwoDList:
    def __init__(self) :
        self.l =[]
        self.n = 0
        self.inn =0
    
    def assigner_list (self):
        n = int (input("ENTER THE RANGE OF THE LIST ="))
        for i in range(n):
            a =[]
            inn = int(input(f"ENTER THE RANGE OF INNER LIST {i} ="))
            for j in range(inn):
                e = input(f"ENTER THE ELEMENT {j} =")
                a.append(e)
            self.l.append(a)
            del a    
            
    def printing(self):
            for h in range(len(self.l)):
                print(*self.l[h],sep=",",end=" ")
                print()
    
    def accession(self):
        a,b,c=eval(input("ENTER SUBSCRIPT ="))
        print(f"THE ELEMENT IS {self.l[a][b][c]}")
    
    def three_d(self):
        tdl = []
        inn = int(input("ENTER THE RANGE OF INNER LIST ="))
        for j in range(inn):
            e = input(f"ENTER THE ELEMENT {j} =")
            tdl.append(e)
        a=eval(input("ENTER SUBSCRIPT ="))
        self.l [a].append(tdl)
        del tdl
        print(self.l)
        tl.printing()
        
tl =TwoDList()
tl.assigner_list()
tl.printing()    
tl.accession()
tl.three_d()