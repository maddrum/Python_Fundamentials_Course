from math import sqrt
from sys import maxsize


class calcPad():
    def __init__(self):
        self.__data = {}
        self.__result_data = {}
        self.__minimum_keys = []

    def delta(self, x1, x2):
        result = pow((x2 - x1), 2)
        return result

    def minimumFinder(self):
        self.min_distance = min(self.__result_data.values())
        self.__minimum_keys = [item for item in self.__result_data if self.__result_data[item] == self.min_distance]
        if len(self.__minimum_keys) > 2:
            minimum_coords = maxsize
            minimum_point_key = 'aaa'
            for item in self.__data:
                coords = self.__data[item]
                current_distance_to_zero = sqrt(pow(coords[0], 2) + pow(coords[1], 2))
                if current_distance_to_zero < minimum_coords:
                    minimum_coords = current_distance_to_zero
                    minimum_point_key = str(item)
            self.__minimum_keys = [item for item in self.__minimum_keys if minimum_point_key in item.split("-")]

    def result(self, data_in):
        self.__data = data_in
        result = []
        for i in data_in:
            for j in data_in:
                if j == i:
                    continue
                point1 = data_in[i]
                point2 = data_in[j]
                deltaX = self.delta(point1[0], point2[0])
                deltaY = self.delta(point1[0], point2[0])
                self.__result_data[str(str(i) + "-" + str(j))] = sqrt(deltaX + deltaY)
        self.minimumFinder()
        return self.__minimum_keys, self.min_distance


n = int(input())
data = {i: list(map(int, input().split())) for i in range(n)}
resultD, min_dist = calcPad().result(data)
print(f'{min_dist:.3f}')
for item in resultD:
    point_id = item.split("-")
    output = data[int(point_id[0])]
    print("(", end="")
    print(*output, sep=", ", end="")
    print(")")
