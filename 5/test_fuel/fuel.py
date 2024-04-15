import sys
def main():

    inputstring = input("Fraction: ")
    print(gauge(convert(inputstring)))

def convert(fraction):

    x, y = fraction.split("/")
    if int(x) > int(y):
        raise ValueError
    elif int(y) == 0:
        raise ZeroDivisionError
    else:
        return (round((int(x) / int(y)) * 100))


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f'{percentage}%'


if __name__ == "__main__":
    main()
