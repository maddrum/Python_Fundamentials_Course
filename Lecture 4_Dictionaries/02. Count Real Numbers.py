array = [float(item) for item in input().split()]
dict = {item: array.count(item) for item in array}
for i in sorted(dict):
    print(f'{i} -> {dict[i]} times')
