from math import ceil

money = float(input())
students = int(input())
lightsaber_price = float(input())
robe_price = float(input())
belt_price = float(input())
student_sabres = ceil(1.10 * students)
free_belts = students // 6
needed_belts = students - free_belts
needed_money = student_sabres * lightsaber_price + needed_belts * belt_price + students * robe_price
if needed_money > money:
    more_money = needed_money - money
    print(f'Ivan Cho will need {more_money:.2f}lv more.')
else:
    print('The money is enough - it would cost {0:.2f}lv.'.format(needed_money))
