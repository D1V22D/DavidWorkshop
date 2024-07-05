def primeAdd():
    prime_list = [2]
    range_prime = int(input("Enter range = "))
    num = 2
    ch = False
    while len(prime_list) < range_prime:
        num += 1
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                ch = False
                break
            else:
                ch = True
        if ch == True:
            prime_list.append(num)

    return prime_list


n = primeAdd()
print(*n,sep=" ,")
print("sum: ",sum(n))
# import math
# n=2
# s = math.sqrt(2)
# s += 1
# print(s)