class FlamesCalculator:
    p1,p2,="",""
    total=0
    
    def __init__(self) :
        self.flames = ['Friend','Love','Affection','Marriage','Enemy','Sibling']
        self.pe1 =""
        self.pe2 =""
        
    def Nameget1(self):
        self.pe1 = input("Enter name 1 =\t")
        # return self.pe1
        
    
    def Nameget2(self):
        self.pe2 = input("Enter name 2 =\t")
        # return self.pe2
        
        
    def Namecheck(self):
        fl.p1=self.pe1.lower()
        fl.p2=self.pe2.lower()
        for i in fl.p1:
            for j in fl.p2:
                if i==j:
                    fl.p1 = fl.p1.replace(i,'',1)
                    fl.p2 = fl.p2.replace(i,'',1)
                    break
                else:
                    continue
        fl.total = len(fl.p1)+len(fl.p2)
        return f"Person 1 =\t{self.pe1}\nPerson 2 =\t{self.pe2}\ntotal ={fl.total}"
    
    
    def FlamesCreater(self,p1,p2,total):
        t = self.flames
        while len(t) > 1 :
            split_index = (total % len(t) - 1)
            if split_index >= 0:
                right = t[split_index + 1:]
                left = t[: split_index]
                t = right + left
            else:
                t = t[: len(t) - 1]
        return t

        
fl = FlamesCalculator()
fl.Nameget1()
fl.Nameget2()
print(fl.Namecheck())
print(fl.FlamesCreater(p1=fl.p1,p2=fl.p1,total=fl.total))



# print(fl.FlamesCreater())
# a = [ 'f','l','a','m','e','s']
# for i in range(8):
#     if len(a)-1>=i:
#         print (a[i])
#     else:
#         print(a[abs((len(a))-i)])
          # if len(t)-1 >= i:
            #     i+=1
            # else:
            #     a = abs((len(t)-1)-tot)-1
            #     if len(t)-1 < a:
            #         tot = tot//2
            #         a = abs((len(t)-1)-tot)-1
            #         del t[a]
            #     else:
            #         del t[a]
            #     i =a 
            #     print(t)