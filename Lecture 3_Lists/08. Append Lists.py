array = input().split("|")
result = [item for item in array[::-1] for item in item.split()]
print(' '.join(result))
