input_data = [int(item) for item in input().split()]
len_data = len(input_data)
for i in range(len_data):
    if input_data[i] >= len_data:
        input_data[i] = input_data[i] % len_data
while len_data > 1:
    control_len = len_data
    dead_indexes = []
    for i in range(len_data):
        if i in dead_indexes:
            continue
        if i == input_data[i] and control_len > 1:
            print(f'{i} performed harakiri')
            dead_indexes.append(i)
            control_len -= 1
            continue
        battle = i - input_data[i]
        if control_len <=1:
            continue
        if battle % 2 == 0:
            dead_indexes.append(input_data[i])
            print(f'{i} x {input_data[i]} -> {i} wins')
        else:
            dead_indexes.append(i)
            print(f'{i} x {input_data[i]} -> {input_data[i]} wins')
        control_len -= 1
    input_data = [input_data[i] for i in range(len_data) if i not in dead_indexes]
    len_data = len(input_data)
    for i in range(len_data):
        if input_data[i] >= len_data:
            input_data[i] = input_data[i] % len_data
