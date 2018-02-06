from math import sqrt


class checker:
    def __init__(self, x, y, width, height):
        self.x1 = x
        self.y1 = y
        self.width = width
        self.height = height
        self.x2 = self.x1 + self.width
        self.y2 = self.y1
        self.x3 = self.x2
        self.y3 = self.y1 + self.height
        self.x4 = self.x1
        self.y4 = self.y3

    def point_inside_check(self, x_in, y_in):
        if x_in >= self.x1 and x_in <= self.x2 and y_in >= self.y1 and y_in <= self.y4:
            return True
        else:
            return False


inputData1 = input().split()
inputData2 = input().split()
rect1 = checker(int(inputData1[0]), int(inputData1[1]), int(inputData1[2]), int(inputData1[3]))
rect2 = checker(int(inputData2[0]), int(inputData2[1]), int(inputData2[2]), int(inputData2[3]))
check_1 = rect2.point_inside_check(rect1.x1, rect1.y1)
check_2 = rect2.point_inside_check(rect1.x2, rect1.y2)
check_3 = rect2.point_inside_check(rect1.x3, rect1.y3)
check_4 = rect2.point_inside_check(rect1.x4, rect1.y4)

if check_1 and check_2 and check_3 and check_4:
    print("Inside")
else:
    print("Not inside")
