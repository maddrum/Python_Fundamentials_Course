def CompStr(b, c):
    if b > c:
        return b
    else:
        return c


def CompNum(b, c):
    if b > c:
        return b
    else:
        return c


a = input()
b = input()
c = input()

if a == "int":
    print(CompNum(b, c))
else:
    print(CompStr(b, c))
