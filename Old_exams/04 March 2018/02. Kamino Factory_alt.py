import re


class data_holder:

    def __init__(self, string, sequence, start, string_raw, input_order_num):
        self.string = str(string)
        self.sequence = int(sequence)
        self.start = int(start)
        self.sum = 0
        self.string_raw = str(string_raw)
        self.sum_calculator()
        self.input_order_num = int(input_order_num)

    def sum_calculator(self):
        list_string = list(map(int, list(self.string)))
        self.sum = sum(list_string)


pattern = r'1+'
regex = re.compile(pattern)
input_order = []
sequence = int(input())
max_sequence_all = -100
i = 1
while True:
    seq_dict = {}
    max_sequence = -100
    sequence_start = -1
    input_data = input()
    if input_data == "Clone them!":
        break
    modified_input_data = input_data.replace("!", "")
    matches = regex.finditer(modified_input_data)
    for match in matches:
        match_split_len = len(match.group(0))
        if match_split_len > max_sequence:
            max_sequence = match_split_len
            sequence_start = match.start()
    if max_sequence_all < max_sequence:
        max_sequence_all = max_sequence
    data_class = data_holder(string=modified_input_data, sequence=max_sequence, start=sequence_start,
                             string_raw=input_data, input_order_num=i)
    input_order.append(data_class)
    i += 1
min_start_number = 100000
max_sum = 0
for item in input_order:
    if item.sequence != max_sequence_all:
        continue
    item_start = item.start
    if min_start_number > item_start:
        min_start_number = item_start
    if item.sum > max_sum:
        max_sum = item.sum
result = [item for item in input_order if item.sequence == max_sequence_all and item.start == min_start_number]
if len(result) > 1:
    result = [item for item in result if item.sum == max_sum]
print(f'Best DNA sample {result[0].input_order_num} with sum: {result[0].sum}.')
DNA_sequence = list(result[0].string)
print(*DNA_sequence, sep=" ")
