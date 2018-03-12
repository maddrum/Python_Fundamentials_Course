trains_data = {}
while True:
    func = ''
    temp_cars_dict = {}
    input_data = input()
    if input_data == "It's Training Men!":
        break
    trains = input_data.split(" -> ")
    if len(trains) != 1:
        car = trains[1].split(" : ")
        if len(car) != 1:
            train_name = trains[0]
            car_name = car[0]
            car_power = car[1]
            func = 'add'
        else:
            func = 'replace'
    equal_trains = input_data.split(" = ")
    if len(equal_trains) != 1:
        func = 'equal'
    if func == 'add':
        if train_name in trains_data:
            temp_cars_dict = trains_data[train_name]
        temp_cars_dict[car_name] = int(car_power)
        trains_data[train_name] = temp_cars_dict
    elif func == 'replace':
        train1_cars = trains_data[trains[1]]
        if trains[0] in trains_data:
            train0_cars = trains_data[trains[0]]
        else:
            train0_cars = {}
        if train1_cars:
            for item in train1_cars:
                train0_cars[item] = train1_cars[item]
        trains_data[trains[0]] = train0_cars
        trains_data.pop(trains[1])
    elif func == 'equal':
        trains_data[equal_trains[0]] = trains_data[equal_trains[1]]
trains_sum = {}
train_car_number = {}
for item in trains_data:
    sum_cars = 0
    i = 1
    temp_cars_dict = trains_data[item]
    for single_item in temp_cars_dict:
        sum_cars += temp_cars_dict[single_item]
        number_of_cars = i
        i += 1
    total_sum = sum_cars * 1000 + number_of_cars
    trains_sum[item] = total_sum

for item in sorted(trains_sum, key=lambda x: (trains_sum[x], x), reverse=True):
    print(f'Train: {item}')
    temp_cars_dict = trains_data[item]
    for single_item in sorted(temp_cars_dict, key=temp_cars_dict.get, reverse=True):
        print(f'###{single_item} - {temp_cars_dict[single_item]}')
