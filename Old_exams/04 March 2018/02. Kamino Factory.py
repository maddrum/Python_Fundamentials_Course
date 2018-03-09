import re

pattern = r'(1!)*'
regex = re.compile(pattern)
data_dict = {}
input_order = {}
sequence = int(input())
i = 1
while True:
    input_data = input()
    if input_data == "Clone them!":
        break
    matches = regex.finditer(input_data)
    max_len = 0
    for match in matches:
        match_split = match.group(0).split("!")
        match_split = [item for item in match_split if item != '']
        match_len = list(map(int, match_split))
        if sum(match_len) > max_len:
            max_len = sum(match_len)
    splitted_input = list(map(int, input_data.split("!")))
    temp_arr = []
    if max_len in data_dict:
        temp_arr = data_dict[max_len]
    temp_arr.append(splitted_input)
    data_dict[max_len] = temp_arr
    stripped_input = input_data.replace("!", "")
    input_order[stripped_input] = i
    i += 1
max_key = max(data_dict)
max_sequences = data_dict[max_key]
data_dict = {}
for item in max_sequences:
    for index in range(0, len(item) - 1):
        dict_temp_arr = []
        if item[index] == 0:
            continue
        last_index = index + max_key
        if last_index > len(item) + 1:
            continue
        else:
            temp_arr = item[index:last_index]
            if sum(temp_arr) == len(temp_arr):
                start_index = index
            else:
                continue
            if start_index in data_dict:
                dict_temp_arr = data_dict[start_index]
            dict_temp_arr.append(item)
            data_dict[start_index] = dict_temp_arr
min_key = min(data_dict)
min_sequence = data_dict[min_key]
min_sequence_string = ""
if len(min_sequence) == 1:
    for item in min_sequence[0]:
        min_sequence_string += str(item)
    min_key = input_order[min_sequence_string]
    print(f'Best DNA sample {min_key} with sum: {sum(min_sequence[0])}.')
    print(*min_sequence[0], sep=" ")
    exit()
max_sum = -100
for item in min_sequence:
    if sum(item) > max_sum:
        max_sum = sum(item)
        max_item = item
for item in max_item:
    min_sequence_string += str(item)
min_key = input_order[min_sequence_string]
print(f'Best DNA sample {min_key} with sum: {max_sum}.')
print(*max_item, sep=" ")
