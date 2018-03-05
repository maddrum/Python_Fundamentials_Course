letter_counter = {}

N = int(input())
input_strings = []
for i in range(N):
    input_strings.append(input())
for item in input_strings:
    list_item = list(set(item))
    for letter in list_item:
        if letter in letter_counter:
            temp = letter_counter[letter]
            temp += item.count(letter)
            letter_counter[letter] = temp
        else:
            letter_counter[letter] = item.count(letter)
for item in sorted(letter_counter, key=letter_counter.get, reverse=True):
    max_letter = item
    break
row = 0
for item in input_strings:
    consecutive_letter_count = 2 * row + 1
    consecutive_letter_string = str(max_letter) * consecutive_letter_count
    replaced_item = item.replace(consecutive_letter_string, " ")
    if replaced_item == item:
        continue
    else:
        row += 1
for i in range(row):
    repeat_number = 2 * i + 1
    print(max_letter * repeat_number)
