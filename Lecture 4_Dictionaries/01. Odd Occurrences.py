array = [i for i in input().lower().split()]
dict = {item: array.count(item) for item in array}
result = [item for item in dict if int(dict[item]) % 2 != 0]
print(", ".join(result))
