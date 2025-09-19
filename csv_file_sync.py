import os
import csv

download_folder = "/home/user/Music/test/"

csv_file = "syntax-error.csv"

playlist_tracks = set()
with open(download_folder + csv_file, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        row = row[:-1]
        print(f"{row[1]} - {row[0]}.mp3")

# Scan download folder
for file in os.listdir(download_folder):
    if file not in playlist_tracks:
        file_path = os.path.join(download_folder, file)
        os.remove(file_path)
        print(f"Deleted: {file}")
