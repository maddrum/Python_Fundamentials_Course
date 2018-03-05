from math import sqrt


class point_coords:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def find_distance_to_point(self, x_in, y_in):
        self.x_check = x_in
        self.y_check = y_in
        distance = sqrt(pow((self.x - self.x_check), 2) + pow((self.y - self.y_check), 2))
        return distance


collection = []
n = int(input())
for i in range(n):
    inputStr = input().split()
    collection.append(point_coords(inputStr[0], inputStr[1]))
distance = {}
for item in collection:
    for item1 in collection:
        if item == item1:
            continue
        key = str(collection.index(item)) + "-" + str(collection.index(item1))
        distance[key] = item.find_distance_to_point(item1.x, item1.y)
for item in sorted(distance, key=distance.get):
    points = item.split("-")
    point1_x = collection[int(points[0])].x
    point1_y = collection[int(points[0])].y
    point2_x = collection[int(points[1])].x
    point2_y = collection[int(points[1])].y
    print(f'{distance[item]:.3f}')
    print(f'({point1_x}, {point1_y})')
    print(f'({point2_x}, {point2_y})')
    break
