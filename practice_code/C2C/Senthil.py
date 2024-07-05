class Task_4:
    def __init__(self):
        self.array = []
        self.sort_array = []
        self.big_gap = 0

    def sortArray(self):
        temp_array = self.array
        n = len(temp_array)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if temp_array[j] > temp_array[j + 1]:
                    temp_array[j], temp_array[j + 1] = temp_array[j + 1], temp_array[j]
        return temp_array

    def findGap(self):
        current = 0
        index1 = 0
        index2 = 1
        while index1 < len(self.sort_array) and index2 < len(self.sort_array):
            self.big_gap = self.sort_array[index2] - self.sort_array[index1]
            if  self.big_gap > current:
                current = self.big_gap
            index1 += 1
            index2 += 1
        return current

    def main(self):
        self.array = list(map(int, input("Enter elements : ").split(" ")))
        print(self.array)
        self.sort_array = T4.sortArray()
        print(self.sort_array)
        print(T4.findGap())


if __name__ == "__main__":
    T4 = Task_4()
    T4.main()
