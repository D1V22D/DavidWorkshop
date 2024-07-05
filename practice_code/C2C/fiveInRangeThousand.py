class FiveInThousand:
    def __init__(self):
        pass

    def Method1(self):
        return [i for i in range(5, 996) if "5" in str(i)]

    def Method2(self):
        a = []
        for i in range(5, 996):
            j = i
            while j > 0:
                digit = j % 10
                if digit == 5:
                    a.append(i)
                j //= 10
        return a

    def Method3(self):
        a = []
        i = 5
        while i >= 5 and i < 996 :
            # a.append(i)
            if i % 5 == 0:
                a.append(i)
            i += 1
        return a

    def main(self):
        print("Method 1:\n", *fit.Method1(), sep=" ")
        print("Method 2:\n", *fit.Method2(), sep=" ")
        print("Method 3:\n", *fit.Method3(), sep=" ")


if __name__ == "__main__":
    fit = FiveInThousand()
    fit.main()
