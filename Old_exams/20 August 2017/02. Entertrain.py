locomotive_power = int(input())
train_cars = []
while True:
    input_data = input()
    if input_data == "All ofboard!":
        break
    train_cars.append(int(input_data))
    train_cars_sum = sum(train_cars)
    if train_cars_sum > locomotive_power:
        mean = train_cars_sum / len(train_cars)
        differences = [abs(item - mean) for item in train_cars]
        minimum_difference = min(differences)
        index_of_min_diff = differences.index(minimum_difference)
        train_cars.pop(index_of_min_diff)
train_cars = train_cars[::-1]
train_cars.append(locomotive_power)
print(*train_cars, sep=' ')
