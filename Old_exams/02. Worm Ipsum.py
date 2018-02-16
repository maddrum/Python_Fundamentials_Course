while True:
    output_string = []
    input_str = input()
    if input_str == "Worm Ipsum":
        break
    dot_counter = input_str.count(".")
    exclamation_counter = input_str.count("!")
    question_counter = input_str.count("?")
    if dot_counter > 1 or exclamation_counter > 1 or question_counter > 1:
        continue
    if dot_counter >= 1:
        if question_counter >= 1:
            continue
        if exclamation_counter >= 1:
            continue
    if question_counter >= 1:
        if dot_counter >= 1:
            continue
        if exclamation_counter >= 1:
            continue
    if exclamation_counter >= 1:
        if dot_counter >= 1:
            continue
        if question_counter >= 1:
            continue

    input_str = input_str.split()
    for item in input_str:
        count_letters = {letter: item.count(letter) for letter in list(item)}
        most_used_letter = max(count_letters, key=count_letters.get)
        if item.count(most_used_letter) > 1:
            if item[-1] in ['.', '!', '?']:
                replaced_word = (len(item) - 1) * most_used_letter + item[-1]
            else:
                replaced_word = len(item) * most_used_letter
            output_string.append(replaced_word)
        else:
            output_string.append(item)
    print(*output_string, sep=" ")
