def primeOrNot():
    k = int(input("Enter a number : "))
    a = ""
    if k == 2:
        a = f"{k} is Prime Number"
    elif k == 1:
        a = f"{k} is Composite"
    else:
        for i in range(2, k):
            if k % i == 0:
                a = f"{k} is Not a Prime Number"
                break
            else:
                a = f"{k} is a Prime Number"
    print(a)


# def primeOnWhile():
#     k = int(input("Enter a number : "))
#     i = 2
#     while k % i != 0:


# primeOrNot()
