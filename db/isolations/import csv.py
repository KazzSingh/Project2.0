import csv


def line_break():
    print("#####################################################################")


people = [{'name': "Kazz", 'age': 31}, {'name': 'Lam', 'age': 33}]

fam = []

with open("fam.csv") as f:
    fam = [{k: v for k, v in row.items()}
           for row in csv.DictReader(f, skipinitialspace=True)]
    print(fam)


line_break()

with open("people.csv", 'w', newline='') as f:
    fieldnames = ['name', 'age']
    writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=',')
    writer.writeheader()
    for row in fam:
        writer.writerow(row)
