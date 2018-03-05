import os

folder_names = ['01. Odd Lines', '02. Line Numbers', '03. Merge Files', '04. Filter-Extensions', '05. HTML Contents',
                '06. User Database', '08. Re-Directory', '09. Products']
if not os.path.isdir("Output"):
    os.mkdir("Output")
os.chdir("./Output")
for item in folder_names:
    if not os.path.isdir(item):
        os.mkdir(item)
