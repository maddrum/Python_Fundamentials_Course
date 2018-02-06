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


inputData1 = input().split()
inputData2 = input().split()
rect1 = checker(int(inputData1[0]), int(inputData1[1]), int(inputData1[2]), int(inputData1[3]))
rect2 = checker(int(inputData2[0]), int(inputData2[1]), int(inputData2[2]), int(inputData2[3]))
if rect1.x2 in range(rect2.x1, rect2.x3 + 1) and rect1.x2 in range(rect2.x1, rect2.x3 + 1) and \
        rect1.y1 in range(rect2.y1, rect2.y3 + 1) and rect1.y1 in range(rect2.y1, rect2.y3 + 1):
    print("Inside")
else:
    print("Not inside")
