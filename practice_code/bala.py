li = []
li1 = []
s = 0
n = int(input("Enter the range : "))
k = int(input("Enter the divisible : "))

# for i in range(n):
#     el = int(input(f"Enter element {i} : "))
#     li.append(el)

# for j in li:
#     if j % 2 == 0 and j % k == 0:
#         s += j
#         # li1.append(j)
# print(f"the even and divisible {k} were {li1}")
# n = eval(input("Enter the list = "))
# print(n)
# print(type(n))

kim = [i for i in range(n) if i % 2 == 0 and i % k == 0]
print(f"the sum is {kim}")
