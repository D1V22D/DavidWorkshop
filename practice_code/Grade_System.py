class GradeSystem:
    def __init__(self):
        self.sub={"Tamil":0,"English":0,"Maths":0,"Science":0,"Social":0}
        self.lt = list(self.sub.keys())
        self.to = 0
        self.avg = 0
    def mark(self):
        for i in range(0,len(self.sub)):
            print("Enter the mark of ",self.lt[i]," :")
            ar = float(input())
            if ar > 0 and ar >=35:
                self.sub[self.lt[i]]=ar
            else :
                print (" !! enter the valid pass mark !!")
                break
    def Average (self):
            man =list (self.sub.values()) 
            self.to=sum(man)
            self.avg = self.to/len(self.lt)
            print("\nTOTAL =",self.to,"\nAVERAGE =",self.avg)
    def Grade (self):
        if (self.avg == 100):
            print(" \nThe grade is O+ ")
        elif 35 <= self.avg and 50 >= self.avg :
            print(" \nThe grade is c ")
        elif 51 <= self.avg and  60 >= self.avg :
            print(" \nThe grade is B ")
        elif 61 <= self.avg and  70 >= self.avg :
            print(" \nThe grade is B+ ")
        elif 71 <= self.avg and  80 >= self.avg :
            print(" \nThe grade is A ")
        elif 81 <= self.avg and  90 >= self.avg :
            print(" \nThe grade is A+ ")
        else :
            print(" \nThe grade is O ")
        print("\n",self.sub,"\n")
n = GradeSystem ()
n.mark()
n.Average()
n.Grade()