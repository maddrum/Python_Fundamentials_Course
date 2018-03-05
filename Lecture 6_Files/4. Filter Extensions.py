import os

input_path = "./Resources/04. Filter-Extensions/input"
all_files = []
for dirs, subdirs, files in os.walk(input_path):
    for item in files:
        all_files.append(item)
input_extension = input()
for item in filter(lambda item_filter: item_filter.split(".")[-1] == input_extension, all_files):
    print(item)
