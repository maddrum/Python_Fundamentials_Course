import os

directory_path = "./Resources/07. Folder Size/TestFolder/"
total_size = 0
for item in os.listdir(directory_path):
    filename = directory_path + item
    if os.path.isfile(filename):
        current_file_size = os.stat(filename).st_size
    else:
        current_file_size = 0
    total_size += current_file_size
total_size_MB = total_size / 1024 / 1024
print(total_size_MB)
