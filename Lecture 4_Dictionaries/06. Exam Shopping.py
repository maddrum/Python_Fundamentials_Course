def stock(name, quantity):
    if name in inventory:
        inventory[name] += quantity
    else:
        inventory[name] = quantity
    return


def buy(name, quantity):
    if name not in inventory:
        print(f'{name} doesn\'t exist')
        return
    if inventory[name] == 0:
        print(f'{name} out of stock')
        return
    if inventory[name] <= quantity:
        inventory[name] = 0
    else:
        inventory[name] -= quantity
    return


inventory = {}
while True:
    inputData = [item for item in input().split()]
    if inputData[0] == "exam" and inputData[1] == "time":
        break
    elif inputData[0] == "stock":
        stock(inputData[1], int(inputData[2]))
    elif inputData[0] == "buy":
        buy(inputData[1], int(inputData[2]))
for item in inventory:
    if inventory[item] != 0:
        print(f'{item} -> {inventory[item]}')
