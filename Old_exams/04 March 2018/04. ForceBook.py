user_side = {}
sides = []
while True:
    input_data = input()
    if input_data == "Lumpawaroo":
        break
    checker = input_data.find("|")
    if checker != -1:
        method = 'check'
        force_side = input_data.split("|")[0].strip()
        force_user = input_data.split("|")[1].strip()
    else:
        method = 'force'
        force_side = input_data.split("->")[1].strip()
        force_user = input_data.split("->")[0].strip()
    if force_side not in sides:
        sides.append(force_side)
    if method == 'check':
        if force_user not in user_side:
            user_side[force_user] = force_side
    else:
        print(f'{force_user} joins the {force_side} side! ')
        user_side[force_user] = force_side
side_users = {item: [] for item in sides}
for item in user_side:
    temp_arr = side_users[user_side[item]]
    temp_arr.append(item)
    side_users[user_side[item]] = temp_arr
for item in sorted(side_users, key=side_users.get, reverse=True):
    if len(side_users[item]) == 0:
        continue
    print(f'Side: {item}, Members: {len(side_users[item])}')
    for single_item in sorted(side_users[item]):
        print(f'! {single_item}')
