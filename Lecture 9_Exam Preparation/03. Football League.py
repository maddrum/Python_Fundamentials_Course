import re

key = re.escape(input())
pattern = f'(.+)?{key}([a-zA-Z]+){key}(.+)?{key}([a-zA-Z]+){key}(.+)(\d+):(\d+)'
regex = re.compile(pattern)
team_goals = {}
team_points = {}
while True:
    temp_team1 = 0
    temp_team2 = 0
    input_str = input()
    if input_str == "final":
        break
    match = regex.search(input_str)
    if match is None:
        continue
    team1 = match.group(2)[::-1].upper()
    team2 = match.group(4)[::-1].upper()
    score1 = int(match.group(6))
    score2 = int(match.group(7))
    try:
        temp_team1 = team_goals[team1]
    except KeyError:
        pass
    try:
        temp_team2 = team_goals[team2]
    except KeyError:
        pass
    temp_team1 += score1
    temp_team2 += score2
    team_goals[team1] = temp_team1
    team_goals[team2] = temp_team2
    if score1 > score2:
        temp_team1 = 3
        temp_team2 = 0
    elif score2 > score1:
        temp_team2 = 3
        temp_team1 = 0
    else:
        temp_team1 = 1
        temp_team2 = 1
    temp_points = 0
    if team1 in team_points:
        temp_points = team_points[team1]
    temp_points += temp_team1
    team_points[team1] = temp_points
    temp_points = 0
    if team2 in team_points:
        temp_points = team_points[team2]
    temp_points += temp_team2
    team_points[team2] = temp_points
team_points_reversed = {}
for item in team_points:
    temp_arr = []
    points = int(team_points[item])
    if points in team_points_reversed:
        temp_arr = team_points_reversed[points]
    temp_arr.append(item)
    team_points_reversed[points] = temp_arr
team_goals_reversed = {}
for item in team_goals:
    temp_arr = []
    points = int(team_goals[item])
    if points in team_goals_reversed:
        temp_arr = team_goals_reversed[points]
    temp_arr.append(item)
    team_goals_reversed[points] = temp_arr
print("League standings:")
i = 1
for item in sorted(team_points_reversed, reverse=True):
    for single_item in sorted(team_points_reversed[item]):
        print(f'{i}. {single_item} {item}')
        i += 1
print("Top 3 scored goals:")
i = 1
sorted_list = sorted(team_goals_reversed, reverse=True)
for item in sorted(team_goals_reversed, reverse=True)[:3]:
    if i == 4:
        break
    for single_item in sorted(team_goals_reversed[item]):
        print(f'- {single_item} -> {item}')
        i += 1
        if i == 4:
            break
