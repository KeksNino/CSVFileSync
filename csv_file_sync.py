import os
import csv

def confirm(prompt="Are you sure? (y/n): "):
    while True:
        ans = input(prompt).strip().lower()
        if ans in ["y", "yes"]:
            return True
        elif ans in ["n", "no"]:
            return False
        else:
            print("Please enter 'y' or 'n'.")

download_folder = "YOUR_FILE_DIRECTORY_PATH"
csv_file = "YOUR_CSV_FILE_PATH"

playlist_tracks = set()
with open(csv_file, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        row = row[:-1]
        new_row = [cell.replace("/", "-") for cell in row]
        filename = f"{new_row[1]} - {new_row[0]}.mp3"
        playlist_tracks.add(filename)

# Scan download folder
for file in os.listdir(download_folder):
    if file not in playlist_tracks:
        file_path = os.path.join(download_folder, file)
        if confirm(f"Delete {file}? (y/n): "):
            os.remove(file_path)
