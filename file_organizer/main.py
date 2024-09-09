import os
from tkinter.filedialog import askdirectory

path = askdirectory(title="choose a folder")

files_list = os.listdir(path)
print(files_list)

local = {
    "images": [".png", ".jpg"],
    "spreadsheets": [".xlsx"],
    "pdfs": [".pdf"],
    "csv": ["csv"],
}

for file in files_list:
    # example: file.pdf
    name, extension = os.path.splitext(f"{path}/{file}")
    for folder in local:
        if extension in local[folder]:
            if not os.path.exists(f"{path}/{folder}"):
                os.mkdir(f"{path}/{folder}")
            os.rename(f"{path}/{file}", f"{path}/{folder}/{file}")