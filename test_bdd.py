import csv;

f= open (r"promotions.csv")
myReader = csv.reader(f)
for row in myReader:
    print(row)