login = {}
counter = 0
while True:
    array = [item for item in input().split(" -> ")]
    if array[0] == "login":
        break
    login[array[0]] = array[1]
while True:
    array = [item for item in input().split(" -> ")]
    if array[0] == "end" and len(array) == 1:
        break
    if array[0] not in login:
        print(f'{array[0]}: login failed')
        counter += 1
    elif login[array[0]] != array[1]:
        print(f'{array[0]}: login failed')
        counter += 1
    else:
        print(f'{array[0]}: logged in successfully')
print(f'unsuccessful login attempts: {counter}')
