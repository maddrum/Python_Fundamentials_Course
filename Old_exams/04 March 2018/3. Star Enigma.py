from re import compile

N = int(input())
messages_enc = [input() for i in range(N)]
messages_decr = []
attacked_planets = []
destroyed_planets = []
for item in messages_enc:
    s_count = item.lower().count("s")
    t_count = item.lower().count("t")
    a_count = item.lower().count("a")
    r_count = item.lower().count("r")
    total_count = s_count + t_count + a_count + r_count
    decr_message = ''
    for letter in item:
        ord_letter = ord(letter)
        decr_ord_letter = ord_letter - total_count
        decr_letter = chr(decr_ord_letter)
        decr_message += decr_letter
    messages_decr.append(decr_message)
pattern = r'@(?P<planet>[A-Za-z]*)(.+)?:(?P<population>\d+)!(?P<attack>[AD])!->(?P<soldier>\d+)'
regex = compile(pattern)
for item in messages_decr:
    matches = regex.finditer(item)
    for match in matches:
        planet = match.group('planet')
        attack = match.group('attack')
        population = int(match.group('population'))
        soldier = int(match.group('soldier'))
        if attack == "A":
            attacked_planets.append(planet)
        else:
            destroyed_planets.append(planet)
print(f'Attacked planets: {len(attacked_planets)}')
for item in sorted(attacked_planets):
    print(f'-> {item}')
print(f'Destroyed planets: {len(destroyed_planets)}')
for item in sorted(destroyed_planets):
    print(f'-> {item}')
