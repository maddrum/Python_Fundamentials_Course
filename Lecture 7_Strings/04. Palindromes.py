input_string = input()
palindromes = list(set([item for item in input_string.split() if item == item[::-1]]))
for item in sorted(palindromes, key=str.lower)[:-1]:
    print(item, end=", ")
print(sorted(palindromes, key=str.lower)[-1])
