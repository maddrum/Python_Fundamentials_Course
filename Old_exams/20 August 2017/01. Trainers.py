N = int(input())
data_dict = {}
for i in range(N):
    distance_to_travel_m = int(input())
    cargo = float(input())
    team = input()
    distance_to_travel = distance_to_travel_m * 1600
    income = 1.5 * cargo*1000 - distance_to_travel * 0.7 * 2.5
    data_dict[team] = income
for item in sorted(data_dict, key=data_dict.get, reverse=True)[:1]:
    print(f'The {item} Trainers win with ${data_dict[item]:.3f}.')
