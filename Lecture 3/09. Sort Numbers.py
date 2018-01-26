array = input().split(" ")
array = [int(i) for i in array]
array.sort()
for i in array[:-1]:
    print(i, end=" <= ")
print(array[-1])
