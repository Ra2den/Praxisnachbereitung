import csv

# Set your file path here
file_path = "/Users/main/Documents/Praxisnachbereitung/excel/Gesamt.csv"

# Read and display the CSV
with open(file_path, "r") as file:
    reader = csv.reader(file)
    
    for row in reader:
        print(row)