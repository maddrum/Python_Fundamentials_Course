from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def CalculateDistance(self, point1, point2):
        self.x1 = point1.x
        self.x2 = point2.x
        self.y1 = point1.y
        self.y2 = point2.y
        distance = int(sqrt(pow((self.x1 - self.x2), 2) + pow((self.y1 - self.y2), 2)))
        return distance


class Rectangle:
    def __init__(self):
        self.area = 0
        self.perimeter = 0

    def CalculatePerimeter(self, width, height):
        if width * height == 0:
            return 0
        self.perimeter = int(2 * width + 2 * height)
        return self.perimeter

    def CalculateArea(self, width, height):
        self.area = int(width * height)
        return self.area


data = {}
counter = 0
while True:
    input_string = input()
    if input_string == "end":
        break
    input_string = input_string.split(" | ")
    collection = [Point(item.split(":")[0], item.split(":")[1]) for item in input_string]
    data.update({counter: collection})
    counter += 1
for item in sorted(data):
    points = data[item]
    width = points[3].CalculateDistance(points[0], points[1])
    height = points[3].CalculateDistance(points[0], points[2])
    area = Rectangle().CalculateArea(width=width, height=height)
    perimeter = Rectangle().CalculatePerimeter(width=width, height=height)
    print(f'Box: {width}, {height}')
    print(f'Perimeter: {perimeter}')
    print(f'Area: {area}')
