class Cricket_Batsman_detector:
    def __init__(self) :
        print(" ***!! WELCOME TO THE BATSMAN CHOOSER !!*** \n")
        self.odd_dict={"1":0,"3":0,"5":0,"7":0,"9":0}
        self.even_dict={"2":0,"4":0,"6":0,"8":0,"10":0}
        self.target=int(input(" TARGET TO ACHIEVE :"))
        self.score=0
        self.bat=0
        self.on_bat={}
        
    def batsman_picker(self):
        print("***  YOUR WISH TO PICK THE ODD OR EVEN BATSMAN ***")
        print("-> 1. ODD \n-> 2. EVEN \n")
        print("\'ENTER AMONG TWO CHOICES \'\n")
        while  True:
            ch=int(input("CHOICE ="))
            if ch == 1:
                n.odd()
                break
            elif ch == 2:
                n.even()
                break
            else:
                print("!! incorrect choice !!")
                continue
    
    def odd(self):
        while self.target >= self.score and self.target != self.score:
            self.bat = int (input ( "-->ENTER THE ODD BATSMAN :"))
            l = str( self.bat )  # noqa: E741
            if len(self.on_bat) != 0 or len(self.on_bat) == 0:
                n.onfield()
                if self.bat % 2 != 0 and self.bat <= 10:
                    for i in range(0,len(self.odd_dict)):
                        if self.bat == int(list(self.odd_dict.keys())[i]):
                            r = self.odd_dict.get(l)
                            self.on_bat[l]=r
                            print(" CURRENT PLAYER :",self.on_bat)
                            del self.odd_dict[l]
                            n.score_pred(l)
                            break
                else:
                    print(" \n!! if you wish to select EVEN batsman !!\n\n ->yes(1) \n ->no(0)")
                    h = int(input( "CHOICE ="))
                    while True:
                        if h == 1:
                            n.even()
                            break
                        elif h == 0:
                            n.odd()
                            break
                        else :
                            continue
                        
                print("OFF THE FIELD :\n",list(self.odd_dict.keys()))
                print("ON THE FIELD :\n",self.on_bat) 
                print("TEAM SCORE :\n",self.score)
                continue
        print(" ** WE WON THE CUP **")
            
    def even(self):
        while self.target >= self.score and self.target != self.score:
            self.bat = int (input ( "-->ENTER THE EVEN BATSMAN :"))
            l = str( self.bat )  # noqa: E741
            if len(self.on_bat) != 0 or len(self.on_bat) == 0:
                n.onfield()
                if self.bat % 2 == 0 and self.bat <= 10:
                    for i in range(0,len(self.even_dict)):
                        if self.bat == int(list(self.even_dict.keys())[i]):
                            r = self.even_dict.get(l)
                            self.on_bat[l]=r
                            print(" CURRENT PLAYER :",self.on_bat)
                            del self.even_dict[l]
                            n.score_pred(l)
                            break
                else:
                    print(" !! if you wish to select ODD batsman !!\n ->yes(1) \n ->no(0)")
                    h = int(input( "CHOICE ="))
                    while True:
                        if h == 1:
                            n.odd()
                            break
                        elif h == 0:
                            n.even()
                            break
                        else :
                            continue
                    
                print("OFF THE FIELD :\n",list(self.even_dict.keys()))
                print("ON THE FIELD :\n",self.on_bat) 
                print("TEAM SCORE :\n",self.score)
                continue
        print(" ** WE WON THE CUP **")
        
    def score_pred(self,l):  # noqa: E741
        e=self.target//10
        r=self.on_bat.get(l)
        q=int(input("RUNS OF ONE BALL :"))
        for i in range(1,e+1):
            r+=q
            if r == self.target :
                break
        self.score=r+self.score
        self.on_bat[l]=r
        print("CURRENT PLAYER SCORE :",r)
        
    def onfield(self):
        if len(self.on_bat) != 0:
            j=0
            for i in range(0+j,len(self.on_bat)):
                if int(list(self.on_bat.keys())[i]) == self.bat:
                    print ("\n!! THE BATSMAN ALREADY ON THE FIELD !!\n")
                    j+=1
                    continue
        # else :
        #     if self.bat % 2 == 0:
        #         break
        #     else:
        #         break
            
 
n=Cricket_Batsman_detector()
n.batsman_picker()                       

   
                
                                 