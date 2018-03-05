class animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age


class dog(animal):
    def __init__(self, name, age, legs):
        animal.__init__(self, name, age)
        self.legs = legs

    def talk(self):
        print("I'm a Distinguishedog, and I will now produce a distinguished sound! Bau Bau.")

    def information(self):
        print(f'Dog: {self.name}, Age: {self.age}, Number Of Legs: {self.legs}')


class cat(animal):
    def __init__(self, name, age, iq):
        animal.__init__(self, name, age)
        self.iq = iq

    def talk(self):
        print("I'm an Aristocat, and I will now produce an aristocratic sound! Myau Myau.")

    def information(self):
        print(f'Cat: {self.name}, Age: {self.age}, IQ: {self.iq}')


class snake(animal):
    def __init__(self, name, age, cruelty):
        animal.__init__(self, name, age)
        self.cruelty = cruelty

    def talk(self):
        print("I'm a Sophistisnake, and I will now produce a sophisticated sound! Honey, I'm home.")

    def information(self):
        print(f'Snake: {self.name}, Age: {self.age}, Cruelty: {self.cruelty}')


dogs = {}
cats = {}
snakes = {}

while True:
    inputLine = input()
    if inputLine == "I'm your Huckleberry":
        break
    inputLine = inputLine.split()
    if inputLine[0] == "Dog":
        dogs.update({inputLine[1]: dog(inputLine[1], inputLine[2], inputLine[3])})
    elif inputLine[0] == "Cat":
        cats.update({inputLine[1]: cat(inputLine[1], inputLine[2], inputLine[3])})
    elif inputLine[0] == "Snake":
        snakes.update({inputLine[1]: snake(inputLine[1], inputLine[2], inputLine[3])})
    elif inputLine[0] == "talk":
        if inputLine[1] in dogs:
            dogs[inputLine[1]].talk()
        elif inputLine[1] in cats:
            cats[inputLine[1]].talk()
        elif inputLine[1] in snakes:
            snakes[inputLine[1]].talk()

for item in dogs:
    dogs[item].information()
for item in cats:
    cats[item].information()
for item in snakes:
    snakes[item].information()
