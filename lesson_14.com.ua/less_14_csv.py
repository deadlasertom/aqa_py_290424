import csv
from pathlib import Path

current_file_path = Path(__file__)
try_csv = current_file_path.parent / "random-michaels.csv"

with open(try_csv) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(",".join(row))

write_csv = current_file_path.parent / "new.csv"
data = [
        ['Name', 'Age', 'City'],
        ['John', 30, 'New York'],
        ['Alice', 25, 'Los Angeles'],
        ['Bob', 35, 'Chicago']
       ]
with open(write_csv, "w", newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=";")
    writer.writerows(data)