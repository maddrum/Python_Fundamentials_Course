array = list(input())
dict = {item: array.count(item) for item in array}
for item in dict:
    print(f'{item} -> {dict[item]} ')
