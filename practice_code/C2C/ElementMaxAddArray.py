class ElementMaxAddArray:
    def __init__(self) :
        self.array = []
        self.index_max = 0

    def getElement(self):
        new_array = list(map(int,input().split(" ")))
        return new_array

    def findMaxIndex(self):
        li = self.array
        li2 = []
        index = 0
        for i in range(len(li)):
            if (li[i]) > index:
                index = li[i]
                li2.append(li[i])
        ind = [i for i,e in enumerate(li) if e == li2[len(li2)-1]]
        ind_final = ind[len(ind) - 1]
        return ind_final

    def addIndex(self, a):
        return a + self.index_max

    def main(self):
        # print("Enter an Array : ")
        self.array = ema.getElement()
        self.index_max = ema.findMaxIndex()
        added_array = list(
            map(
                ema.addIndex,
                self.array,
            )
        )
        print(*added_array,sep=" ")


if __name__ == "__main__":
    ema = ElementMaxAddArray()
    ema.main()
