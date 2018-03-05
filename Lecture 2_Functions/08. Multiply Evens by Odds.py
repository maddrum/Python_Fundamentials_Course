def even_sum(values):
    sumE = 0
    for i in values:
        if i.isdigit():
            if int(i) % 2 == 0:
                sumE += int(i)
    return sumE


def odd_sum(values):
    sumO = 0
    for i in values:
        if i.isdigit():

            if int(i) % 2 != 0:
                sumO += int(i)
    return sumO


userInput = input()
values = list(userInput)
result = odd_sum(values) * even_sum(values)
print(result)
