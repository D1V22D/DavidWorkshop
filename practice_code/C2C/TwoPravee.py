mobile_number = "9880127431"
result = ""
total = 0
for i in range(len(mobile_number)):
    current_digit = int(mobile_number[i])
    if i == 0:
        total = current_digit
    else:
        if current_digit % 2 == int(mobile_number[i - 1]) % 2:
            total += current_digit
        else:
            result += str(total)
            total = current_digit
result += str(total)
print(result)
# # def Calculate(m, n):
# #     sum = 0
# #     for num in range(m, n + 1):
# #         if num % 3 == 0 and num % 5 == 0:
# #             sum += num
# #     return sum
# # m = int(input("m: "))
# # n = int(input("n: "))
# # result = Calculate(m, n)
# # print(result)
# # print(f"The sum of numbers divisible by both 3 and 5 between {m} and {n} is: {result}")