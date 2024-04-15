import sys

if len(sys.argv) > 2 or len(sys.argv) < 2:
    sys.exit("1 command line argument allowed")
if not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")

try:
    with open(sys.argv[1], "r") as file:
        counter = 0
        for line in file:
            if line.lstrip().startswith("#"):
                next

            elif line.lstrip() == "":
                next
                
            else:
                counter+= 1
    print(counter)


except FileNotFoundError:
    sys.exit("File does not exist")
