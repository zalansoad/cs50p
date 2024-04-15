import sys
from tabulate import tabulate
import csv

if not len(sys.argv) == 2:
    sys.exit("1 command line argument allowed")
if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

try:
    with open(sys.argv[1]) as file:

        reader = csv.reader(file)
        print(tabulate(reader, headers="firstrow", tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File does not exist")
