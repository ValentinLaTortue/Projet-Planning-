import csv

csv_file_path = 'test1.csv'

data = {}

with open(csv_file_path, mode='r', newline='') as csvfile:
    csvreader = csv.DictReader(csvfile)

    for row in csvreader:
        course_name = row['nom']
        data[course_name] = {
            'duree': int(row['duree']),
            'listePromo': row['listePromo'].split(';')
        }

print(data)
