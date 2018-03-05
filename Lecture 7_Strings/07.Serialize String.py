input_string = input()
used_array = []
index = -1
for letter in input_string:
    index_array = []
    if letter in used_array:
        continue
    used_array.append(letter)
    while True:
        index = input_string.find(letter, index + 1)
        if index == -1:
            break
        index_array.append(index)
    print(f'{letter}:', end="")
    print(*index_array, sep="/")
