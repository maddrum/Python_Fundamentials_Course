import math


class Coordinates():
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)


userInput = input().split()
point1 = Coordinates(userInput[0], userInput[1])
userInput = input().split()
point2 = Coordinates(userInput[0], userInput[1])
deltaX = pow((point2.x - point1.x), 2)
deltaY = pow((point2.y - point1.y), 2)
distance = math.sqrt(deltaX + deltaY)
print(f'{distance:.3f}')
