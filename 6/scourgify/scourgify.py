import sys
import csv


if not len(sys.argv) == 3:
    sys.exit("2 CLA needed")
if not sys.argv[1].endswith(".csv") and not sys.argv[2].endswith(".csv"):
    sys.exit("Not a CSV file")

try:
    hplist = []
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            hplist.append(row)

except FileNotFoundError:
    sys.exit("File does not exist")

try:
    with open(sys.argv[2], 'w') as afterfile:
        fieldnames = ['first', 'last', 'house']

        writer = csv.DictWriter(afterfile, fieldnames=fieldnames)
        writer.writeheader()
        for item in hplist:
            writer.writerow({'first': item['name'].split(',')[1].lstrip(), 'last':item['name'].split(',')[0].lstrip(), 'house':item['house']})

except FileNotFoundError:
    sys.exit("File does not exist")


