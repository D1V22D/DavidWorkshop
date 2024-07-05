class String_Manipulation:
    def __init__(self):
        self.clg = input("Enter your college Name : ")
        self.size = len(self.clg)

    def Method1(self):
        return self.clg[::2]

    def Method2(self):
        s = ""
        for i in range(self.size):
            if i % 2 == 0:
                s += self.clg[i]
        return s

    def Method3(self):
        s = ""
        # dividend = divisor*quotient-reminder
        for i in range(self.size):
            q = i // 2
            if i - 2 * q == 0:
                s += self.clg[i]
        return s

    def Method4(self):
        s = ""
        for i, a in enumerate(self.clg):
            if i % 2 == 0:
                s += a
        return s

    def Method5(self):
        s = ""
        for i in range(0, self.size, 2):
            s += self.clg[i]
        return s

    def Method6(self):
        s = ""
        for i in range(self.size-1,-1,-2):
            s += self.clg[i]
        return s[::-1]
    
    def main(self):
        print(stn.Method1())
        print(stn.Method2())
        print(stn.Method3())
        print(stn.Method4())
        print(stn.Method5())
        print(stn.Method6())


if __name__ == "__main__":
    stn = String_Manipulation()
    stn.main()
