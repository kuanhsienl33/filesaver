import os
import shutil
import time
path = r"C:/path-to-ideal-folder/"
file_name = os.listdir(path)
folder_names = ['xlsx files', 'image files', 'pdf files', 'word files']

for loop in range (0,4):
    if not os.path.exists(path + folder_names[loop]):
        os.makedirs((path + folder_names[loop]))
for file in file_name:
    if ".xlsx" in file and not os.path.exists(path + "xlsx files/" + file):
        shutil.move(path + file, path + "xlsx files/" + file)
    elif ".JPG" in file and not os.path.exists(path + "image files/" + file):
        shutil.move(path + file, path + "image files/" + file)
    elif ".pdf" in file and not os.path.exists(path + "pdf files/" + file):
        shutil.move(path + file, path + "pdf files/" + file)
    elif ".docx" in file and not os.path.exists(path + "word files/" + file):
        shutil.move(path + file, path + "word files/" + file)
