def triangle(a,h):
    return a*h/2
a = float(input())
b = float(input())
c = triangle(a,b)
print("{0:.12g}".format(c))