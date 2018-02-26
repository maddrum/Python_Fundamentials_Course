import os

filename = input()
points = {}
if not os.path.isfile(filename):
    print("INVALID INPUT")
    exit()
with open(filename) as input_file:
    for read_line in input_file:
        read_line = read_line.split(",")
        read_line[3] = read_line[3].split("\n")[0]
        if read_line[2] == 'gold':
            given_points = 7
        elif read_line[2] == 'silver':
            given_points = 3
        elif read_line[2] == 'bronze':
            given_points = 1
        try:
            points[read_line[3]]
            current_points = points[read_line[3]]
        except KeyError:
            current_points = 0
        current_points += given_points
        points[read_line[3]] = current_points
for item in sorted(sorted(points, reverse=True), key=points.get, reverse=True):
    print(item)
