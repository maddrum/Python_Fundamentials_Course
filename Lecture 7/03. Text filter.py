filter_words = input().split()
string_to_filter = input()
filtered_string = string_to_filter
for item in filter_words:
    stars_number = len(item)
    filtered_string = filtered_string.replace(item, "*" * stars_number)
print(filtered_string)
