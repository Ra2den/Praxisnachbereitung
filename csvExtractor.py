import csv

file_path = "excel/Gesamt-Bereinigt.csv"

with open(file_path, "r") as file:
    reader = csv.reader(file)
    
    for row in reader:
        print(row)