def parameterSign(number):
    if number > 0:
        print(f'The number {number} is positive.')
    elif number < 0:
        print(f'The number {number} is negative.')
    else:
        print(f'The number {number} is zero.')


c = int(input())
parameterSign(c)
