class ri:
    a=[]
    def read():
        n1=0
        n2=int(input("list range:"))
        for i in range(n1,n2+1):
            b=int(input("enter the list:"))
            ri.a=ri.a.append(b)
        print(ri.a)
ri.read()    
        
