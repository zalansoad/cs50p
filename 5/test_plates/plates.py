def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if check(s):
        if zero(s) == 0:
            return False
        if not s[-1].isdigit():
            return False
        if not s[len(s)-counter(s): len(s)].isdigit():
            return False
    #no special symbols
    if not s.isalnum():
        return False
    #Min 2 char
    elif not len(s) >= 2:
        return False
    #first two char exists
    elif not s[0:2].isalpha():
        return False
    #max length
    elif len(s) > 6:
        return False
    else:
        return True

def zero(s):
    for letter in s:
        if letter.isdigit():
            return int(letter)
    return False

def check(s):
    for letter in s:
        if letter.isdigit():
            return True
    return False

def counter(s):
    digits = 0
    for letter in s:
        if letter.isdigit():
            digits += 1
    return digits


if __name__ == "__main__":
    main()
