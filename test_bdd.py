import csv;

f= open (r"Projet-Planning-/promotions.csv")
myReader = csv.reader(f)
for row in myReader:
    print(row)
