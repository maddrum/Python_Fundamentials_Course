import re

sentence_pattern = r'^[A-Z][^\.!\?]*[\.\!\?]$'
regex = re.compile(sentence_pattern)
filter_string = input()
filter_string_letter = filter_string[0]
filter_string_number = int(filter_string[1])
found_words = []
while True:
    sentence = input()
    if sentence == 'end':
        break
    checker = regex.match(sentence)
    if checker == None:
        continue
    words = re.findall(r'\w+\b', sentence)
    for word in words:
        word_counter = word.count(filter_string_letter)
        if word_counter == filter_string_number:
            found_words.append(word)
print(*found_words, sep=", ")
