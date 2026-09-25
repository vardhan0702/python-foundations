import csv
with open("testdata.txt","r")as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)