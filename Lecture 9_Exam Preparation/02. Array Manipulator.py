input_list = [int(item) for item in input().split(" ")]
while True:
    command = input()
    if command == 'end':
        break
    commands = command.split(" ")
    if commands[0] == 'exchange':
        index = int(commands[1])
        if index > len(input_list) - 1 or index < 0:
            print("Invalid index")
            continue
        left_part = input_list[:index + 1]
        right_part = input_list[index + 1:]
        input_list = right_part + left_part
    elif commands[0] == 'max' or commands[0] == 'min':
        even_odd = commands[1]
        if even_odd == "even":
            filtered_items = [item for item in input_list if item % 2 == 0]
        else:
            filtered_items = [item for item in input_list if item % 2 != 0]
        if not filtered_items:
            print("No matches")
            continue
        if commands[0] == 'max':
            needed_value = max(filtered_items)
        else:
            needed_value = min(filtered_items)
        index = input_list[::-1].index(needed_value)
        index = len(input_list) - index - 1
        print(index)
    elif commands[0] == "first" or commands[0] == "last":
        even_odd = commands[2]
        count = int(commands[1])
        if count > len(input_list):
            print("Invalid count")
            continue
        if even_odd == "even":
            filtered_items = [item for item in input_list if item % 2 == 0]
        else:
            filtered_items = [item for item in input_list if item % 2 != 0]
        result = filtered_items[:count]
        print(result)
print(input_list)
