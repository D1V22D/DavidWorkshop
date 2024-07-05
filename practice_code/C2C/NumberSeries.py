def SquareSeries():
    n = int(input("n = "))
    sq = 1
    sum = 0
    end0 = ""
    for ind in range(1, n + 1):
        sum = sum + sq
        end0 = end0 + f" {ind}^{2} +"
    sq = (n * (n + 1) * (2 * n + 1)) // 6
    return end0[: len(end0) - 1] + "= " + str(sq)


def NumberSeries():
    count = 0
    exp = 0
    inc = 1
    ran = int(input("n = "))
    for i in range(0,ran):
        exp = i + inc
        count += 1
        if count == 3:
            inc *= 3
            count = 0
        print(exp)


def main():
    print(SquareSeries())
    print(NumberSeries())


main()
