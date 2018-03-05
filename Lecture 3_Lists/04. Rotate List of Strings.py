array = input().split(" ")
a = array[-1]
array.insert(0, a)
array.pop(-1)
print(' '.join(array))
