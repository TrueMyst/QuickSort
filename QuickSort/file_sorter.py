import os
import json
import shutil

download_dir = os.path.expanduser("~/Downloads")

# Accessing the JSON File
with open("./utility/file_ext.json") as f:
    ext_folder = json.load(f)

# Create the destination folders if they don't already exist
for folder in ext_folder.values():
    folder_path = os.path.join(download_dir, folder)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Sort the files in the download directory
for filename in os.listdir(download_dir):
    file_path = os.path.join(download_dir, filename)

    if os.path.isfile(file_path):
        _, ext = os.path.splitext(filename)
        ext = ext.lower()

        if ext in ext_folder:
            dest_folder = ext_folder[ext]
            dest_path = os.path.join(download_dir, dest_folder, filename)
            shutil.move(file_path, dest_path)

print("✅ - Sorted and organized all files in the Downloads directory!")
    