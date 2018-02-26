from math import sqrt
import os

filename = input()
minimum_distance = input()
try:
    minimum_distance = float(minimum_distance)
except ValueError:
    print("INVALID INPUT")
    exit()
coordinates = {}
key_list = []
if not os.path.isfile(filename):
    print("INVALID INPUT")
    exit()
with open(filename) as input_file:
    for read_line in input_file:
        read_line = read_line.split(",")
        try:
            read_line[2] = read_line[2].split("\n")[0]
            coordinates[int(read_line[0])] = [float(read_line[1]), float(read_line[2])]
        except IndexError:
            print("INVALID INPUT")
            exit()
        key_list.append(int(read_line[0]))
counter = 0
checker = True
for i in range(len(key_list)):
    counter += 1
    try:
        current_key = key_list[i]
        next_key = key_list[i + 1]
    except IndexError:
        break
    x1 = coordinates[current_key][0]
    y1 = coordinates[current_key][1]
    x2 = coordinates[next_key][0]
    y2 = coordinates[next_key][1]
    distance = sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2))
    if distance < minimum_distance:
        checker = False
        print(next_key)
if checker:
    print(f'NO CLOSE POINTS FOUND; RECORDS COUNT: {counter}')
