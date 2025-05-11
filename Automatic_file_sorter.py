import os
import shutil
import time
path = r"C:/path-to-ideal-folder/"
file_name = os.listdir(path)
folder_names = ['xlsx files', 'image files', 'pdf files', 'word files']

while True:
    # 1) compute seconds until next 12:00 PM
    now = time.localtime()
    seconds_since_midnight = now.tm_hour*3600 + now.tm_min*60 + now.tm_sec
    # target is 12*3600 seconds; modulo 86400 wraps to tomorrow if past noon
    wait_secs = (12*3600 - seconds_since_midnight) % 86400
    print(f"Waiting {wait_secs//3600}h {(wait_secs%3600)//60}m until next run at 12:00")
    time.sleep(wait_secs)

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

print(f"Sorted files at {time.strftime('%Y‑%m‑%d %H:%M:%S')}\n")
