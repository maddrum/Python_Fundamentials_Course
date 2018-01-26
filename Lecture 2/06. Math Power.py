def power(a, h):
    c = pow(a, h)
    return c


a = float(input())
b = float(input())
c = power(a, b)
print("{0:.12g}".format(c))
