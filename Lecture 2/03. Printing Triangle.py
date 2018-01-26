def printer(n):
    for i in range(1, n + 1):
        print(str(i) + " ", end="")
    print()


def trianglePrint(number):
    for i in range(1, number + 1):
        printer(i)


def reverseTrianglePrint(number):
    for i in reversed(range(1, number)):
        printer(i)


c = int(input())
trianglePrint(c)
reverseTrianglePrint(c)
