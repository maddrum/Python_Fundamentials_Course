age = {}
salary = {}
position = {}
checkFloat = False
while True:
    array = [item for item in input().split(" -> ")]
    if array[0] == "filter base" or len(array) == 1:
        break
    try:
        float(array[1])
        checkFloat = True
    except:
        checkFloat = False
    if checkFloat:
        if float(array[1]) % 1 == 0:
            age[array[0]] = array[1]
        else:
            salary[array[0]] = array[1]
    else:
        position[array[0]] = array[1]
criteria = input()
if criteria == 'Age':
    for item in age:
        print(f'Name: {item}')
        print(f'Age: {age[item]}')
        print('=' * 20)
elif criteria == 'Salary':
    for item in salary:
        print(f'Name: {item}')
        print(f'Salary: {salary[item]}')
        print('=' * 20)
elif criteria == 'Position':
    for item in position:
        print(f'Name: {item}')
        print(f'Position: {position[item]}')
        print('=' * 20)
