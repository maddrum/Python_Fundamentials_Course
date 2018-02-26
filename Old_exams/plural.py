input_str = list(input())
if not input_str:
    print("INVALID INPUT")
    exit()
if input_str[-1] == "y":
    input_str.pop()
    temp = list('ies')
    input_str += temp
elif input_str[-1] in ['s', 'o', 'x', 'z']:
    temp = list('es')
    input_str += temp
elif input_str[-1] == 'h' and (input_str[-2] == 's' or input_str[-2] == 'c'):
    temp = list('es')
    input_str += temp
else:
    input_str.append("s")

print(*input_str, sep='')
