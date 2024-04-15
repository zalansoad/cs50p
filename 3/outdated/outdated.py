months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


while True:
    try:
        date = input("Date: ")
        if "/" in date:
            month, day, year = date.split("/")
            if 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
                print(int(year), f"{int(month):02}", f"{int(day):02}", sep="-")
                break
        else:
            month, day, year = date.split()
            if len(day) == 2:
                day = day.removesuffix(",")
                if month in months and 1 <= int(day) <= 31:
                    print(int(year), f"{int(months.index(month) + 1):02}", f"{int(day):02}", sep="-")
                    break
    except ValueError:
        pass

    except EOFError:
        print("\n", end="")
        break


