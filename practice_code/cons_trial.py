class trial :
    l=[1,1,2,3]
    def __init__(self,l):
        self.l=l
    def remove(self,l):
        n = trial(l)
        n.l=n.l.append(9)
n=trial()
n.remove(n.l)


