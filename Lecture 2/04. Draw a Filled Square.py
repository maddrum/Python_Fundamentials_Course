def printer(number):
    d = number * 2
    print("-" * d)
    for i in range(0, number - 2):
        print("-" + "\\/" * ((d - 1) // 2) + "-")
    print("-" * d)


c = int(input())
printer(c)
