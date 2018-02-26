input_string = input()
upper_case_letters = [ord(item) for item in input_string if item.isupper()]
lower_case_letters = [ord(item) for item in input_string if item.islower()]
condition = input()
if condition == "UPPERCASE":
    sum_ord = sum(upper_case_letters)
    print(f'The total sum is: {sum_ord}')
else:
    sum_ord = sum(lower_case_letters)
    print(f'The total sum is: {sum_ord}')
