# class ElementMaxAdd:
#     def __init__(self):
#         self.array = []
#         self.index_max = tuple()

#     def getElement(self):
#         new_array = list(map(int,input().split(" ")))
#         return new_array

#     def findMaxIndex(self):
#         li = self.array
#         li2 = []
#         index = 0
#         for i in range(len(li)):
#             if (li[i]) > index:
#                 index = li[i]
#                 li2.append(li[i])
#         ind = [index for index, char in enumerate(li) if char == li2[len(li2)-1]]
#         return tuple(li2[len(li2)-1],ind[len(ind)])

#     def addIndex(self, a):
#         return a + self.index_max[1]

#     def main(self):
#         # print("Enter an Array : ")
#         self.array = ema.getElement()
#         self.index_max = ema.findMaxIndex()
#         added_array = list(
#             map(
#                 ema.addIndex,
#                 self.array,
#             )
#         )
#         print(*added_array,sep=" ")


# if __name__ == "__main__":
#     ema = ElementMaxAdd()
#     ema.main()
def add_max_position_to_elements(arr):
    max_element = max(arr)
    max_position = max(i for i, val in enumerate(arr) if val == max_element)

    result = [val + max_position for val in arr]
    return result


# Sample Testcase 1
input_1 = [3, 1, 79, 12, 65]
output_1 = add_max_position_to_elements(input_1)
print("Sample Testcase 1")
print("Input:", " ".join(map(str, input_1)))
print("Output:", " ".join(map(str, output_1)))
print()

# Sample Testcase 2
input_2 = [3, 1, 79, 12, 79, 65]
output_2 = add_max_position_to_elements(input_2)
print("Sample Testcase 2")
print("Input:", " ".join(map(str, input_2)))
print("Output:", " ".join(map(str, output_2)))
