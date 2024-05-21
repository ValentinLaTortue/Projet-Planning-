import csv

matieres = {}

with open('Matières.csv', mode='r', newline='') as csvfile:
    csvreader = csv.DictReader(csvfile)

    for row in csvreader:
        course_name = row['nom']
        matieres[course_name] = {
            'duree': int(row['duree']),
        }

promotions = {}

with open('Promotions.csv', mode='r', newline='') as csvfile:
    csvreader = csv.DictReader(csvfile)

    for row in csvreader:
        course_name = row['nom']
        promotions[course_name] = {
            'nb_eleves': int(row['nb_eleves']),
            'liste_matieres': row['liste_matieres'].split(';')
        }
