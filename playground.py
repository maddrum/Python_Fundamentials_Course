import random
for i in range(10):
    a = -50
    b = 50
    x1 = random.randint(a,b)
    x2 = random.randint(a,b)
    y1=random.randint(a,b)
    y2=random.randint(a,b)
    string = f'{x2}:{y2} | {x1}:{y1} | {x2}:{y1} | {x1}:{y2}'
    print(string)
    print("end")
