input_string = input()
open_diamonds = input_string.count("<") + 1
current_start_diamond_index = -1
current_end_diamond_index = 0
checker = True
last_end_index_checker = False
for i in range(0, open_diamonds):
    carat = 0
    cycle_check = False
    current_start_diamond_index = input_string.find("<", current_start_diamond_index + 1)
    if current_start_diamond_index != -1:
        current_end_diamond_index = input_string.find(">", current_end_diamond_index + 1)
    else:
        current_end_diamond_index = -1
    if current_start_diamond_index >= current_end_diamond_index:
        continue
    for index in range(current_start_diamond_index, current_end_diamond_index + 1):
        cycle_check = True
        if input_string[index].isdigit():
            carat += int(input_string[index])
    if carat == 0 and cycle_check:
        checker = False
        print('Found 0 carat diamond')
    if carat != 0:
        checker = False
        print(f'Found {carat} carat diamond')
if checker:
    print("Better luck next time")
