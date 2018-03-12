N = int(input())
cards_dict = {}
tickets_dict = {}
name_sum_dict = {}
name_card_dict = {}
for i in range(N):
    input_data = input()
    input_data_split = input_data.split()
    name = input_data_split[0] + " " + input_data_split[1]
    card = input_data_split[2]
    temp_arr = []
    if name in cards_dict:
        temp_arr = cards_dict[name]
    temp_arr.append(card)
    cards_dict[name] = temp_arr
    name_card_dict[card] = name
while True:
    card_not_to_another = True
    input_data = input()
    if input_data == "time to leave!":
        break
    input_data_split = input_data.split()
    name = input_data_split[1] + " " + input_data_split[2]
    destination = input_data_split[3]
    card_number = input_data_split[4]
    ticket_price = 0
    for item in destination:
        ticket_price += ord(item)
    ticket_price = ticket_price / 100
    sum_card_number = 0
    # проверка на картата
    for item in card_number:
        sum_card_number += int(item)
    if sum_card_number % 7 == 0:
        valid_checker = True
    else:
        valid_checker = False
        print(f'card {card_number} is not valid!')
    if card_number in name_card_dict:
        if name != name_card_dict[card_number]:
            print(f'card {card_number} already exists for another passenger!')
            card_not_to_another = False
    if name in tickets_dict:
        temp_dict = tickets_dict[name]
    else:
        temp_dict = {}
    if name in cards_dict:
        temp_arr = cards_dict[name]
    else:
        temp_arr = []
    if name in cards_dict:
        if card_number in cards_dict[name] and card_not_to_another:
            temp_dict[destination + "@" + card_number] = ticket_price * 0.5
        elif valid_checker and card_not_to_another:
            print(f'issuing card {card_number}')
            temp_arr.append(card_number)
            name_card_dict[card_number] = name
            temp_dict[destination + "@" + card_number] = ticket_price * 0.5
    elif valid_checker and card_not_to_another:
        print(f'issuing card {card_number}')
        temp_arr.append(card_number)
        temp_dict[destination + "@" + card_number] = ticket_price * 0.5
        name_card_dict[card_number] = name
    else:
        temp_dict[destination] = ticket_price
    if len(temp_arr) != 0:
        cards_dict[name] = temp_arr
    tickets_dict[name] = temp_dict
    temp_sum = 0
    for item in temp_dict:
        temp_sum += temp_dict[item]
    name_sum_dict[name] = temp_sum
for item in sorted(name_sum_dict, key=name_sum_dict.get, reverse=True):
    print(f'{item}:')
    temp_dict = tickets_dict[item]
    temp_sum = 0
    for single_item in sorted(temp_dict, key=temp_dict.get, reverse=True):
        single_item_split = single_item.split("@")
        if len(single_item_split) > 1:
            destination = single_item_split[0]
            card_number = single_item_split[1]
            print(f'--{destination}: {temp_dict[single_item]:.2f}lv (using card {card_number})')
        else:
            print(f'--{single_item}: {temp_dict[single_item]:.2f}lv')
        temp_sum += temp_dict[single_item]
    print(f'total: {temp_sum:.2f}lv')
