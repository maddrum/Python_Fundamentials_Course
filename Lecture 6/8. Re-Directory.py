from shutil import copyfile
import os

input_folder = "./Resources/08. Re-Directory/input"
output_folder = "./Output/08. Re-Directory"
extensions = set([item.split(".")[-1] for item in os.listdir(input_folder)])
summarized_files = {item: [] for item in extensions}
for item in summarized_files:
    temp_arr = [file for file in os.listdir(input_folder) if file.split(".")[-1] == item]
    summarized_files[item] = temp_arr
for item in summarized_files:
    folder_name = item + "s"
    destination_folder = output_folder + "/" + folder_name
    os.mkdir(destination_folder)
    for file in summarized_files[item]:
        source = input_folder + "/" + file
        destination = destination_folder + "/" + file
        copyfile(source, destination)
