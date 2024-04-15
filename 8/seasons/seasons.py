from datetime import date, datetime
import inflect
import sys
import re

class Calculator:
    def __init__(self):
        self.today = date.today()

    @classmethod
    def get(cls):
        date = input("Date of Birth: ")
        match =  re.search(r"^\d{4}-\d{2}-\d{2}$", date)
        if match:
            return date
        else:
            sys.exit("Invalid date")

    @classmethod
    def conversion(cls, date):
        p = inflect.engine()
        birth = datetime.strptime(date, '%Y-%m-%d').date()
        result = str((cls().today - birth).days * 24 * 60)
        string = p.number_to_words(result, andword="")
        return f'{string.capitalize()} minutes'




def main():
    date = Calculator.get()
    print(Calculator.conversion(date))


if __name__ == "__main__":
    main()
