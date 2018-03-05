from math import sqrt

array = input().split(" ")
square = [int(i) for i in array if int(i) > 0 if sqrt(int(i)) % 1 == 0]
square.sort(reverse=True)
for i in square:
    print(i, end=" ")
