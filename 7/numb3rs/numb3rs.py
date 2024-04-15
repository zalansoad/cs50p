import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    ...

    matches =  re.search(r"^(\d+\d?\d?)\.(\d+\d?\d?)\.(\d+\d?\d?)\.(\d+\d?\d?)$", ip)

    try:
        a, b, c, d = matches.groups()
        list = [int(a), int(b), int(c), int(d)]
        counter = 0
        for number in list:
            if number > 255:
                counter += 1

        if counter > 0:
            return False
        else:
            return True

    except AttributeError:
        return False



if __name__ == "__main__":
    main()
