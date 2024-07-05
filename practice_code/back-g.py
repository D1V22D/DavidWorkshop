class David_Resume:
    def __init__(self) -> None:
        self.job = True
        self.intern = True
        if self.intern == True:
            self.getIntern()
        else:
            self.getJob()
        
    def getJob(self):
        print("get the call letter")
    def getIntern(self):
        print("get job after intern")
        self.getJob()
        
resume = David_Resume()