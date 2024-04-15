def main():
    camelCase = input("camelCase: ")
    sanek_case(camelCase)

def sanek_case(camelCase):
    for letter in camelCase:
        if letter.isupper():
            letter = "_" + letter.lower()
            print(letter, end="")
        else:
            print (letter, end="")
    print()

main()

