def Another():
    print("Odd :")
    for i in range(31, 40, 2):
        print(i)
    print("Even :")
    for i in range(80, 91, 2):
        print(i)


def Logical():
    n = int(input("Enter the range :"))
    for i in range(1, n + 1):
        if i % 2 == 0 and i >= 30 and i <= 40:
            continue
        elif i % 2 != 0 and i >= 80 and i <= 90:
            continue
        else:
            print(i)
            # continue


def mul(s, l):
    for i in l:
        s = s * i
    return s


def Eleven_Nine():
    a = [x for x in range(1, 300) if x % 11 == 0 and x % 9 == 0]
    print(a)
    print(mul(s=1, l=a))

def factors(l):
    fac = []
    for i in range(len(l)):
        for j in range(1,l[i]):
            if l[i]%j == 0 :
                fac.append(j)
    return set(fac)

def Five_Seven_Eleven ():
    s = int(input("Enter the start : "))
    e = int(input("Enter the end : "))
    d1 = int(input("Enter the divisible 1 : "))
    d2 = int(input("Enter the divisible 2 : "))
    nd = int(input("Enter Non divisible : "))
    a = [x for x in range(s,e) if x % d1 == 0 and x % d2 == 0 and x % nd!= 0 ]
    print(f"\nThe list of divisible of {d1} , {d2} and Non divisible of {nd} :")
    print(a,sep=",")
    print("\nThe List of factors :")
    print(factors(l=a),sep=",")

def First_and_last():
    a = int(input("enter a number ="))
    l = a%10
    f = a
    while l>10:
        l //= 10
    print("first =",f)
    print("last =",l)


def digitAnalyzer():
    # num = int(inp)
    pass
# Logical()
# Another()
# Eleven_Nine()
Five_Seven_Eleven()
# First_and_last()
# and x % 11 == 0