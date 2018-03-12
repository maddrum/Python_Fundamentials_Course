import operator


class Card:
    def __init__(self, name_in, number):
        self.name = name_in
        self.number = number


class Trips:
    def __init__(self, name_in, destination_in, price, card_in):
        self.name = name_in
        self.destination = destination_in
        self.price = price
        if card != "N/A":
            self.card = card_in
        else:
            self.card = 'N/A'


cards_dict = {}
tickets_dict = {}
name_sum_dict = {}
N = int(input())
for i in range(N):
    input_data = input()
    input_data_split = input_data.split(" ")
    name = input_data_split[0] + " " + input_data_split[1]
    card = input_data_split[2]
    class_card = Card(name_in=name, number=card)
    cards_dict[card] = class_card
while True:
    not_another_user = True
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
    for item in card_number:
        sum_card_number += int(item)
    if sum_card_number % 7 == 0:
        valid_checker = True
    else:
        valid_checker = False
        print(f'card {card_number} is not valid!')
    if valid_checker:
        if card_number in cards_dict:
            class_data = cards_dict[card_number]
            if class_data.name == name:
                not_another_user = True
            else:
                not_another_user = False
                print(f'card {card_number} already exists for another passenger!')
    if valid_checker and not_another_user:
        if card_number not in cards_dict:
            data_class = Card(name_in=name, number=card_number)
            cards_dict[card_number] = data_class
            print(f'issuing card {card_number}')
        ticket_price = ticket_price * 0.5
        if name in tickets_dict:
            temp_arr = tickets_dict[name]
        else:
            temp_arr = []
        class_data = Trips(name_in=name, destination_in=destination, price=ticket_price, card_in=card_number)
        temp_arr.append(class_data)
    else:
        if name in tickets_dict:
            temp_arr = tickets_dict[name]
        else:
            temp_arr = []
        class_data = Trips(name_in=name, destination_in=destination, price=ticket_price, card_in="N/A")
        temp_arr.append(class_data)
    tickets_dict[name] = temp_arr
    if name in name_sum_dict:
        total_trip_money = name_sum_dict[name]
    else:
        total_trip_money = 0
    total_trip_money += ticket_price
    name_sum_dict[name] = total_trip_money
for item in sorted(name_sum_dict, key=name_sum_dict.get, reverse=True):
    print(f'{item}:')
    data_class_arr = tickets_dict[item]
    temp_sum = 0
    for single_item in sorted(data_class_arr, key=operator.attrgetter('price'), reverse=True):
        if single_item.card != "N/A":
            print(f'--{single_item.destination}: {single_item.price:.2f}lv (using card {single_item.card})')
        else:
            print(f'--{single_item.destination}: {single_item.price:.2f}lv')
        temp_sum += single_item.price
    print(f'total: {temp_sum:.2f}lv')
