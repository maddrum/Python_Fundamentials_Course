inputStr = input()
str_l = len(inputStr)
array = list(inputStr)
array = [item for item in array if item == "(" or item == ")"]
counter = 0

if "(" not in array and ")" not in array:
    print("INVALID INPUT")
    quit()
if "(" not in array or ")" not in array:
    print(f'WRONG {str_l}')
    quit()
if array.index(")") < array.index("("):
    print(f'WRONG {str_l}')
    quit()

while array.index("(") < array.index(")"):
    array = [item for item in array if item != 0]
    for i in range(len(array)):
        if array[i] == "(" and array[i + 1] == ")":
            array[i] = 0
            array[i + 1] = 0
            counter += 1
    if "(" not in array or ")" not in array:
        break
array = [item for item in array if item != 0]
if array:
    print(f'WRONG {str_l}')
else:
    print(f'OK {counter}')
